import math 
from numpy import *

def noyauGaussien(v1, v2, sigma):

	if sigma != 0 :
		if len(v1) == len(v2):
			return math.exp(0 - dot(array(v1) - array(v2), array(v1) - array(v2)) ** 2 / sigma ** 2)
		else :
			print "error taille v1 != taille v2"
	else :
		print "error sigma = 0"
		

def noyauPolynomial(v1, v2, k):

	if len(v1) == len(v2):
		return (1 + dot(v1, v2)) ** k
	else :
		print "error taille v1 != taille v2"


def computeGram(data, kernel, h):

	nex,nfeat = data.shape

	G = zeros(shape=(nex,nex))
	for i in range(nex):
		for j in range(nex):
			G[i][j] = kernel(data[i], data[j], h)
	
	return G

