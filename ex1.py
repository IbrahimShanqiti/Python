from sys import argv
from os.path import exists
from PIL import Image
import numpy
import math
script = argv
name_of_file = input("What is the name of your file? (exlude the .txt)")
image = open(f"{name_of_file}.txt", 'r')
width = (image.readline())
height = (image.readline())
aaa = (image.readline())
aab = (image.readline())
aac = (image.readline())

data = numpy.zeros((int(width), int(height), 3), dtype=numpy.uint8)

data[0, 0] = [int(aaa),int(aab),int(aac)]


image = Image.fromarray(data)
image = image.save('Image.png')
