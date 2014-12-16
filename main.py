from noyau import *
from perceptron import *
from image import *
from numpy import *
from projetM1 import *

kernel = 0
h = 1.

def assemble(mer, autre):

	merTarget = ones(len(mer))
	autreTarget = [-1.] * len(autre)
	
	data = concatenate((mer, autre))
	target = concatenate((merTarget,autreTarget))
	
	return data, target

def histogramTest(kernel, h):

	print "Histogramme: kernel =", kernel," h =", h
	
	imHist = importImageHist()
	
	merHist = histMatrixFromDir('Data/Mer/')
	autreHist = histMatrixFromDir('Data/Ailleurs/')
	
	data, target = assemble(merHist, autreHist)

	alpha = learnKernelPerceptron(data, target, kernel, h)
	for i in range(len(imHist)):
		print predictKernelPerceptron(alpha, data, target, imHist[i], kernel, h)




def vectorTest(kernel, h):

	print "Vecteur: kernel =", kernel," h =", h
	
	imVect = importImageVect()
	
	merVect = vectMatrixFromDir('Data/Mer/')
	autreVect = vectMatrixFromDir('Data/Ailleurs/')
	
	data, target = assemble(merVect, autreVect)
	
	alpha = learnKernelPerceptron(data, target, kernel, h)
	for i in range(len(imVect)):
		print predictKernelPerceptron(alpha, data, target, imVect[i], kernel, h)
	
	
vectorTest(kernel, h)
#histogramTest(kernel, h)
