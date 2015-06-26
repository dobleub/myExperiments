#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
  Copyright 2012 Paul C. Brown <bro666@gmail.com>.
    
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Load modules

from optparse import OptionParser
import Image
import ImageFont, ImageDraw
import random
import string
import os

import codecs

from string import maketrans
from django.utils.encoding import smart_str, smart_unicode


# Class
class make_animation:
  def __init__ (self, vText, vFont, vColor, vSize, vKeyframes, vDuration, vFps=25):
    random.seed()
    self.frameCounter=0
    self.text=vText
    self.color=vColor
    self.size=vSize
    self.font = ImageFont.truetype(vFont, vSize)
    self.keyframes=int(vKeyframes)
    self.fps=vFps
   
    self.fpKeyframe=int((int(vDuration)*self.fps)/self.keyframes)
  
  # Calculate size of frame ( width of "W" x number of letters, height of "hy")
  
  def parse_Geometry(self, vGeometry):
    self.geometry=str.split(str.split(vGeometry,"x")[1],"+")
    self.geometry.insert(0, str.split(vGeometry,"x")[0])
    
    self.geometry = map(int, self.geometry)

    
    """
	self.geometry[0] > Frame width
	self.geometry[1] > Frame height
	self.geometry[2] > Offset x
	self.geometry[3] > Offset y
    """
    
  
  # Create strings
  
  def create_Strings(self):
    self.strings=[]
    variations=[]
    pickFrom=string.letters + string.digits
  
  #	Pick random tranforms between 1 and frames for each letter
    for i in self.text:
      variations.append(random.randrange(0,self.keyframes))
    
    variations[random.randrange(0,len(self.text))]=self.keyframes
    
    for i in range(self.keyframes):
      temptext=""
      for j in range(len(variations)):
	
	if (variations[j]>0):
	  temptext=temptext + pickFrom[random.randrange(0,len(pickFrom))]
	  variations[j]-=1
	else:
	  temptext=temptext + unicode(self.text[j].encode('utf-8'), 'utf-8')

      print (smart_str(temptext))	    
      self.strings.append(temptext)
      
  
  #	Build each new string and put into tuples
    self.strings.append(self.text)
  
  
  
  # Itearte over tuple and make frame for each
  def make_Frames(self, vEpilogue=0):
    for i in self.strings:
      for j in range(self.fpKeyframe):
	self.make_Frame(i)
	
    for i in range(self.fps*vEpilogue):
      self.make_Frame(self.text)
      
  
  # Create one frame per string
  
  def make_Frame(self, vText):
    vIm = Image.new("RGBA", self.geometry[:2])
    draw = ImageDraw.Draw(vIm)
    draw.text(self.geometry[2:], vText, font=self.font, fill=self.color)
    vIm.save("frame" + str(self.frameCounter).zfill(4) + ".png","PNG")
    self.frameCounter+=1

    
  
  # Mount film
  
  def make_Film(self, vMovie):
    os.system("ffmpeg -qscale 5 -r " + str(self.fps) + " -b 9600 -i frame%04d.png -vcodec png " + vMovie + ".mov && rm -f frame*.png")


# Main

if __name__ == '__main__':

  # Grab input text
  parser = OptionParser()
  parser.add_option("-t", "--text", help="Text to be 'imaged'", dest="vText", default="Hello")
  parser.add_option("-c", "--color", help="#RRGGBB", dest="vColor", default="#FFFFFF")
  parser.add_option("-k", "--keyframes", help="Number of frames untill message appears complete. NOTE: NOT the same as number of frames in movie. Does not include final completed frame.", dest="vKeyframes", default=10)
  parser.add_option("-f", "--font", help="Path to font. Works best with monospace.", dest="vFont", default="/usr/share/fonts/liberation/LiberationMono-Regular.ttf")
  parser.add_option("-s", "--size", help="Font size.", dest="vSize", default=12)
  parser.add_option("-d", "--duration", help="Duration of effect (in seconds).", dest="vDuration", default=3)
  parser.add_option("-x", "--fps", help="Frames per second.", dest="vFps", default=25)
  parser.add_option("-g", "--geometry", help="Size of frame and offset of text within frame: wxh+px+py (e.g. -g 1024x768+10+10)", dest="vGeometry", default="1024x768+10+10")
  parser.add_option("-e", "--epilogue", help="How long the last frame will remain on screen in seconds", dest="vEpilogue", default=0)
  parser.add_option("-o", "--output", help="Name of output file (without extension -- generates MOV movie with alpha).", dest="vMovie", default="movie")

  (options, args) = parser.parse_args()
  
  vText=unicode(options.vText, 'utf-8')

  a=make_animation(vText=vText, vFont=options.vFont, vColor=options.vColor, vSize=int(options.vSize), vKeyframes=options.vKeyframes, vDuration=options.vDuration)
  
  a.create_Strings()
  a.parse_Geometry(options.vGeometry)
  a.make_Frames(int(options.vEpilogue))
  a.make_Film(options.vMovie)