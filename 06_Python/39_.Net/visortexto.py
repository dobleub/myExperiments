import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.IO import *
from System.Drawing import Color, Point
from System.Windows.Forms import (Application, BorderStyle, Button, Form, FormBorderStyle, Label, Panel, Screen, OpenFileDialog, DialogResult, TextBox, ScrollBars)

class LectorTXT(Form):
 def __init__ (self):
  self.Text = "Visor de texto Linux Magazine"
  self.FormBorderStyle = FormBorderStyle.FixedDialog

  pantalla =  Screen.GetWorkingArea(self)
  self.Height = 300
  self.Width = 400
  
  self.panel1 = Panel()
  self.panel1.Location = Point (0,0)
  self.panel1.Width = self.Width
  self.panel1.Height = self.Height
  self.panel1.BorderStyle = BorderStyle.FixedSingle

  self.generaLabel1()
  self.generaLabel2()
  self.generaBoton1()
  self.generaAreaTexto()

  self.panel1.Controls.Add(self.label1)
  self.panel1.Controls.Add(self.label2)
  self.panel1.Controls.Add(self.boton1)
  self.panel1.Controls.Add(self.areaTexto)

  self.Controls.Add(self.panel1)

 def generaAreaTexto(self):
  texto = TextBox()
  texto.Height = self.Height / 2
  texto.Width = self.Width - 30 # para que no se salga
  texto.Location = Point(20,110)
  texto.Multiline = True
  texto.ScrollBars = ScrollBars.Vertical
  self.areaTexto = texto

 def generaLabel1(self):
  self.label1 = Label()
  self.label1.Text = "Lector de ficheros de texto Linux Magazine"
  self.label1.Location = Point(20,20)
  self.label1.Height = 25
  self.label1.Width = self.Width 

 def generaLabel2(self):
  self.label2 = Label()
  self.label2.Text = "Fichero seleccionado: ??"
  self.label2.Location = Point(20,50)
  self.label2.Height = 25
  self.label2.Width = self.Width

 def generaBoton1(self):
  self.boton1 = Button ()
  self.boton1.Name= 'Botón 1'
  self.boton1.Text = 'Abrir fichero'
  self.boton1.Location = Point(20,80)
  self.boton1.Height = 25
  self.boton1.Width = 100
  self.boton1.Click += self.abreFichero

 def abreFichero(self, sender, event):
  color = OpenFileDialog()
  color.Filter = "Ficheros txt (*.txt)|*.txt"
  color.Title = "Selecciona un fichero de texto"

  nombre = ""
  
  if (color.ShowDialog() == DialogResult.OK ):
   nombre = color.FileName
   self.label2.Text = "Fichero seleccionado: " + nombre
# cargamos el texto
   fichero =  File.OpenText(nombre)
   texto = ""

   s = fichero.ReadLine()
   while s :
    texto +=  s
    s = fichero.ReadLine()
  
   self.areaTexto.Text = texto

form = LectorTXT()

Application.Run(form)