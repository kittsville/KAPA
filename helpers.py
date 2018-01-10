from matplotlib import pylab
import kapa
import random

def create_antigen(name):
    image_matrix = pylab.imread('digits/' + name + '.png')
    shape = []

    for row in image_matrix:
        shape += [all(pixel) == 0 for pixel in row] # Converts colour to boolean (black = True)

    return kapa.Antigen(shape)

def create_antibody():
    return kapa.Antibody([random.random() >= .5 for s in range(120)])
