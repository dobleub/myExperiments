import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import Color, Point
from System.Windows.Forms import (Application, BorderStyle, Button, Form, FormBorderStyle, Label, Panel, Screen)

class HolaMundo(Form):
 def __init__ (self):
  self.Text = "Hola Linux Magazine"
  self.FormBorderStyle = FormBorderStyle.FixedDialog

  pantalla =  Screen.GetWorkingArea(self)
  self.Height = pantalla.Height / 5
  self.Width = pantalla.Width / 5
  
  self.panel1 = Panel()
  self.panel1.Location = Point (0,0)
  self.panel1.Width = self.Width
  self.panel1.Height = self.Height

  self.generaSaludo()

  self.panel1.Controls.Add(self.label1)
  self.Controls.Add(self.panel1)

 def generaSaludo(self):
  self.label1 = Label()
  self.label1.Text = "Hola lectores de Linux Magazine"
  self.label1.Location = Point(20,20)
  self.label1.Height = 25
  self.label1.Width = self.Width 

form = HolaMundo()
Application.Run(form)