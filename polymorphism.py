  #---------------------------------------------------new file----------------super.py----------------------------------------------------#

class Animal:
  def __init__(self, eyecolor, height):
    self.eyecolor = eyecolor
    self.height = height
    
  #---------------------------------------------------new file----------------sub.py----------------------------------------------------#
    
from Super import Animal

class Zebra(Animal):
  def __init__(self, eyecolor, height, name):
    super().__init__(eyecolor, height)
    self.name = name
    
  #---------------------------------------------------new file---------------main.py----------------------------------------------------#  
    
from Sub import Zebra
from Super import Animal

animals = []

animals.append(Animal("green", 12))
animals.append(Zebra("White",12,"Marty"))

for Zebra in animals:
  print(Zebra.name)
