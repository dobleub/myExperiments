#!/usr/bin/python

# ---NOTA--------------------------------------
# El fichero que debe ser pasado como argumento
# debe consistir en un listado con una url por
# línea. 
# ---------------------------------------------

class Lista_URLs:
    """Recibe un fichero y carga sus cadenas en una lista. Provee de métodos para obtener de nuevo las cadenas desde la lista."""
    
    def __init__(self,nombre):
        # La lista donde guardaremos las URLs
        self.lista= []
        # El contador que usaremos para comprobaciones
        self.contador = 0

        # pasamos el nombre del fichero menos el último carácter
        self.archivo = file(nombre)
        self.cadena = self.archivo.readline()

        while(self.cadena != '\n'):
            #Metemos la cadena en la lista
            self.lista.append(self.cadena)
            self.cadena = self.archivo.readline()
        self.archivo.close()
        

    def rebobina(self):
        # Hace que se comience de nuevo
        # por el principio en la lista.
	self.contador = 0
        

    def siguiente(self):
        # Devuelve el siguiente elemento o
        # '' en caso de llegar al final.
        if ( self.contador >= len(self.lista)):
            return ''
        else: 
            self.valor = self.lista[self.contador]
            self.contador = self.contador + 1
            return self.valor

    def fin(self):
        # Comprueba que hemos llegado al final
        # de la lista. Preguntamos si hemos llegado
        # al final antes de avanzar.
        return (self.contador == len(self.lista))

def crea_directorio(cadena):
    # Comprueba si el directorio especificado por
    # cadena existe, en caso contrario lo crea
    # y cambia el directorio de trabajo
    # al directorio creado.
    
    componentes = cadena.split('.')

    if(os.path.exists(componentes[0])):
	print "Error: el directorio ya existe"
        sys.exit()
    else:	
	# Creamos el directorio
	os.makedirs(componentes[0])
        os.chdir(componentes[0])
        print 'Creando directorio ' + componentes[0]

def descarga_urls(lista):
    # Recorre la lista de urls usando el objeto
    # Lista_URLs, las descarga y después las
    # guarda en ficheros con el mismo nombre que
    # el de la imagen.

    lista.rebobina()

    while( not lista.fin() ):
        url = lista.siguiente()

        # dividimos la url en dos partes
        # lo que descargamos y la url http

        # Componentes es una lista que contiene
        # las cadenas resultantes de trocear la
        # cadena de texto de la URL usando '/'
        # como separador. Por ejemplo:
        # http://www.python.org/index.html
        # componentes = ['http:', '', 'www.python.org',
        #                'index.html']
        componentes = url.split('/')
        servidor = componentes[2]

        # Construimos la ruta de la imagen, que
        # consiste en toda la ruta si eliminamos
        # al servidor y a http://
        ruta_imagen = '/'
        for i in range( 3,  len(componentes)):
            ruta_imagen = ruta_imagen + '/' + componentes[i]

        # Descarga el fichero y lo guarda con el nombre.
        # El nombre se saca de la URL.
        # url[:-1] es la cadena url menos el último carácter. 
        print 'Descargando imagen: ' + url[:-1]
        conexion = httplib.HTTPConnection(servidor)
        conexion.request("GET", ruta_imagen)
        respuesta = conexion.getresponse()
        # datos contiene ahora la imagen y la guardamos
        datos = respuesta.read()
        conexion.close()
            
        # el nombre del fichero es el último elemento
        # de la lista componentes
        nomb_fichero = componentes[len(componentes) -1]
        # eliminamos el \n final
        nomb_fichero = nomb_fichero[:-1]

        # Abrimos el fichero, escribimos y cerramos
        archivo = file(nomb_fichero ,'w')
        archivo.write(datos)
        archivo.close()

def genera_index(lista):

    # Crea un fichero index.html.
    # Genera la cabecera, recorre la lista de URLS
    # y por último escribe el pie.
    # Es posible mejorarlo introduciendo separadores
    # o títulos entre las imágenes ;)

    print 'Generando índice index.html'

    archivo = file('index.html','w')

    # Cabecera
    archivo.write('<html>\n')
    archivo.write('<head>\n')
    archivo.write('<title> Imagenes </title>\n')
    archivo.write('</head>\n')
    archivo.write('<body>\n')
    archivo.write('<h1>Imagenes</h1>\n')
    archivo.write('<ul>\n')

    # siempre antes de recorrer:
    lista.rebobina()
    url = lista.siguiente()

    # Dividimos la URL para poder utilizar
    # partes de ella.
    componentes = url.split('/')
    imagen = componentes[len(componentes) - 1] 

    # Recorremos las urls
    while( url != ''):
        # Imagen en HTML
        archivo.write('<li><img src=\"'+ imagen +'\"></img></li>\n')      
        url = lista.siguiente()
        componentes = url.split('/')
        imagen = componentes[len(componentes) - 1]

    # ... y por último el pie.

    archivo.write('</ul>\n')
    archivo.write('</body>\n')
    archivo.write('</html>\n')
    
    archivo.close()

#---------------------------------------------------
# Main
#---------------------------------------------------

# Esta es la técnica estándar para organizar el
# código en Python, se usa la siguiente construcción
# como punto de arranque.

if __name__ == '__main__':

    import httplib
    import os
    import os.path
    import sys

    # Comprobamos los argumentos...

    if len(sys.argv) == 2:
        #Pasamos el fichero al constructor
        lista = Lista_URLs(sys.argv[1])


        crea_directorio(sys.argv[1])

        descarga_urls(lista)
      
        genera_index(lista)

    elif len(sys.argv) == 0:
        # Vaya, han ejecutado sin poner argumentos...
        # les recordaremos como va esto ;)
        print 'La sintaxis del programa es:\n'
        print sys.argv[0] + ' archivo\n'
        print 'El archivo debe contener una URL por línea'  
        
    else:
        # Alguien se ha quedado corto y se ha pasado
        # con el número de argumentos.
        print "ERROR: la sintaxis es " + sys.argv[0] + " <fichero>"