from noyau import *
from perceptron import *
from image import *
from numpy import *
from projetM1 import *

# Auteurs: Sarah BOUKRIS et Ismael CUSSAC
# Option IAA Master 1 - 2014-2015

#Concatene les images de l'echantillon d'apprentissage (mer et autre)
def assemble(mer, autre):

	merTarget = ones(len(mer))
	autreTarget = [-1.] * len(autre)
	
	data = concatenate((mer, autre))
	target = concatenate((merTarget, autreTarget))
	
	return data, target

#Construit le perceptron a partir des donnees puis predit la classe de l'echantillon
def predit(data, target, im, kernel, h):

	alpha, echec = learnKernelPerceptron(data, target, kernel, h, 10000)

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

#Execute le programme avec les histogrammes
def histogramTest(kernel):

	imHist = importImageHist()
	merHist = histMatrixFromDir('Data/Mer/')
	autreHist = histMatrixFromDir('Data/Ailleurs/')
	
	data, target = assemble(merHist, autreHist)
	
	h = trouveHyperParam(data, target)
	print "Histogramme: kernel =", kernel," h =", h
	predit(data, target, imHist, kernel, h)
	
#Execute le programme avec les images vectorisees
def vectorTest(kernel):

	imVect = importImageVect()
	merVect = vectMatrixFromDir('Data/Mer/')
	autreVect = vectMatrixFromDir('Data/Ailleurs/')
	
	data, target = assemble(merVect, autreVect)

	h = trouveHyperParam(data, target)
	print "Vecteur: kernel =", kernel," h =", h
	predit(data, target, imVect, kernel, h)
	
	
if __name__ == '__main__':

	kernel = noyauPolynomial
	k = input("Choix du kernel (1-Gaussien / 2-Polynomial): ")
	if k == 1 :
		kernel = noyauGaussien
	
	t = input("Choix du test (1-Vecteur / 2-Histogramme): ")
	if t == 1 :
		vectorTest(kernel)
	else :
		histogramTest(kernel)


