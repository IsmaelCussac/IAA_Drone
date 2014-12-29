from noyau import *
from perceptron import *
from image import *
from numpy import *
from projetM1 import *

#kernel = noyauGaussien
kernel = noyauPolynomial
h = 1.

def assemble(mer, autre):

	merTarget = ones(len(mer))
	autreTarget = [-1.] * len(autre)
	
	data = concatenate((mer, autre))
	target = concatenate((merTarget,autreTarget))
	
	return data, target


def predit(data, target, im, kernel, h):

	alpha, echec = learnKernelPerceptron(data, target, kernel, h)
	if echec:
		return
	T = zeros(len(im))
	for i in range(len(im)):
		T[i] = predictKernelPerceptron(alpha, data, target, im[i], kernel, h)
	print "Classes predites: \n", T


def trouveHyperParam(data, target):
	h, err = bestHyperparametre(data, target, kernel)
	print "Erreurs :"
	print err
	print "Erreur moyenne:", err.mean()
	print "Best hyperparametre =", h
	return h


def histogramTest(kernel, h):

	print "Histogramme: kernel =", kernel," h =", h
	
	imHist = importImageHist()
	merHist = histMatrixFromDir('Data/Mer/')
	autreHist = histMatrixFromDir('Data/Ailleurs/')
	
	data, target = assemble(merHist, autreHist)
	h = trouveHyperParam(data, target)
	predit(data, target, imHist, kernel, h)
	

def vectorTest(kernel, h):

	print "Vecteur: kernel =", kernel," h =", h
	
	imVect = importImageVect()
	merVect = vectMatrixFromDir('Data/Mer/')
	autreVect = vectMatrixFromDir('Data/Ailleurs/')
	
	data, target = assemble(merVect, autreVect)
	h = trouveHyperParam(data, target)
	predit(data, target, imVect, kernel, h)
	

	
vectorTest(kernel, h)
#histogramTest(kernel, h)


