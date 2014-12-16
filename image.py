from PIL import Image
from numpy import *
import os, sys


def vectImage(directory, nom):

	im = Image.open(directory + nom).resize((32,32))
	mat = array(im)
	return reshape(mat, (1, 32*32*3))

	
def vectMatrixFromDir(directory):

	images = os.listdir(directory)
	V = zeros(shape=(len(images),32*32*3))
	
	i = 0
	for image in images:
		V[i] = vectImage(directory, image)
		i = i + 1
		
	return V
	
	
def histImage(directory, nom):

	im = Image.open(directory + nom)
	width, height = im.size
	return array(im.histogram()) / (1.0 * width * height)
	
	
def histMatrixFromDir(directory):

	images = os.listdir(directory)
	H = zeros(shape=(len(images),256*3))
	
	i = 0
	for image in images:
		H[i] = histImage(directory, image)
		i = i + 1
	
	return H
	
V = vectMatrixFromDir('Data/Mer/')
H = histMatrixFromDir('Data/Mer/')


