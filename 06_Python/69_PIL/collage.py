#!/usr/local/bin/python
#
# Realizado por José María Ruiz Aguilera (2005)
# josemaria@ieee.org 
#
# Derechos reservados
######################################################

import Image
import httplib
import cStringIO
import ConfigParser
import re

class Imagen:
    def __init__(self,titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
        self.coord_X1 = 0
        self.coord_Y1 = 0
        self.coord_X2 = 0 
        self.coord_Y2 = 0

class Collage:

    def __init__(self):
        # Aquí guardaré todo
        self.hashImagenes = {}

	self.__cargaConf()

        for url in self.hashImagenes.keys():
            self.__descarga(url)

    def __cargaConf(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('collage.conf'))

        self.maxX = config.getint('tamaño','horizontal')
        self.maxY = config.getint('tamaño','vertical')

        opciones = config.options('imágenes')

        for opcion in opciones:
            self.hashImagenes[opcion] = config.get('imágenes',opcion)
   
    def __descarga(self, llave):
        url = self.hashImagenes[llave]
        # Eliminamos el "http://"
        cadena1 = url.split('http://')[1]
        # Nos quedamos con la máquina
        m = re.match('[a-zA-Z\n\.\-]+', cadena1)
        cadena1 = m.group()
        # Y ahora con la ruta
        cadena2 = m.string[m.end():]

        try:
            # Transacción HTTP
            con = httplib.HTTPConnection(cadena1)
            con.request("GET", cadena2)
            resp = con.getresponse()

            if (resp.status == 200):
                datos = resp.read()
                self.hashImagenes[llave] = Imagen(cadena2.split("/").pop(),
                                                  Image.open(cStringIO.StringIO(datos)))
            else:
                print "Ha ocurrido un error cuando se trataba de descargar " + cadena1 + cadena2
                #  eliminamos del hash
                del self.hashImagenes[llave]
                print "Razón: "+resp.reason

        except:
            print "[Excepción]: Ha ocurrido un error cuando se trataba de descargar " + cadena1 + cadena2
            #Algo ha ido mal
            del self.hashImagenes[llave]

    def __totalXY(self):
        # Devuelve e
        suma = [0,0]
        for imagen in self.hashImagenes.itervalues():
            suma[0] = suma[0] + imagen.contenido.size[0]
            suma[1] = suma[1] + imagen.contenido.size[1]
        return suma

    def generaCollage(self):
        self.__generaImagen()
        self.__generaHTML()

    def __generaImagen(self):
        # Regla de 3, si
        total = self.__totalXY()
        imagenFinal = Image.new('RGB',(self.maxX,self.maxY))

        # Calculamos el tamaño de las cuadrículas

        num_imagenes = len(self.hashImagenes)
        particiones = 2
        
        while ( (particiones*particiones) < num_imagenes):
            particiones = particiones * 2

        # Tenemos el número de particiones, así que las cuadrículas serán
        # (maxX / particiones) x (maxY /particiones)

        cuadricula = ((self.maxX / particiones), (self.maxY / particiones))
        contX = 0
        contY = 0
                
        for imagen in self.hashImagenes.iteritems():
            # Ya tenemos las nuevos parámetros, ahora escalamos

            imagen[1].contenido.save(imagen[1].titulo)
            nueva_imagen = imagen[1].contenido.copy()
            nueva_imagen.thumbnail(cuadricula,Image.ANTIALIAS)

            #¿Cómo posicionamos?, cuando contX es > que particiones,
            # se incrementa contY y se pone a 0 contX. O sea, bajamos
            # a la siguiente fila.
            if (contX == particiones):
                contX = 0
                contY = contY + 1

            # Calculamos las coordenadas finales en el collage
            imagen[1].coord_X1 = contX * cuadricula[0]
            imagen[1].coord_Y1 = contY * cuadricula[1]
            imagen[1].coord_X2 = imagen[1].coord_X1 + cuadricula[0]
            imagen[1].coord_Y2 = imagen[1].coord_Y1 + cuadricula[1]
            
            imagenFinal.paste(nueva_imagen, (imagen[1].coord_X1, imagen[1].coord_Y1))

            contX = contX + 1  # siguiente cuadrícula

        imagenFinal.save("collage.png")

    def __generaHTML(self):
        indice = file("index.html","w+")
        
        # Cabecera
        indice.write("<html>\n"+
        "<head>\n"+
        "<title>Collage de Imágenes</title>\n"+
        "</head>\n"+
        "<body>\n"+
        "<h1>Collage de Imágenes</h1>\n"+
        "<img src=\"collage.png\"  usemap=\"#mapa\">\n"+
        "<map name=\"mapa\">\n")

        for i in self.hashImagenes.iteritems():
            nombre = i[1].titulo
            
            indice.write("<area shape=\"rect\" alt=\""+
                         nombre + "\" "+
                         "href=\""+ nombre +
                         "\"  coords=\""+
                         str(i[1].coord_X1) + "," +
                         str(i[1].coord_Y1) + "," +
                         str(i[1].coord_X2) + "," +
                         str(i[1].coord_Y2) + "\" />\n")
                                     
        # Pie
        indice.write("</map>\n"+
                     "</object>\n"+
                     "</body>\n"+
                     "</html>\n")
        indice.close()

if __name__ == "__main__":
    c = Collage()
    c.generaCollage()