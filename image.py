from PIL import Image
from numpy import *
import os, sys


def vectImage(directory, nom):
	im = Image.open(directory + nom).resize((32,32))
	#print im.size, im
	mat = array(im)
	#print mat.shape, mat
	vect = reshape(mat, (1, 32*32*3))

	return vect
	
def vectMatrixFromDir(directory):
	images = os.listdir(directory)
	V = zeros(shape=(len(images),32*32*3))
	
	i = 0
	for image in images:
		V[i] = vectImage(directory, image)
		i = i + 1
		
	print V
	
vectMatrixFromDir('Data/Mer/')
