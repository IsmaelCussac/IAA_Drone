import math 
from numpy import *
from noyau import *
from sklearn import cross_validation

sample = array([[3.5,0.5],[2.5,2.],[4.5,1.5],[5.,2.5],[6.,4.],[2.5,3.5],[1.,4.],[2.,6.5],[4.,5.5]])
target = array([-1,-1,-1,-1,-1,1,1,1,1])

t_sample= array([[2.,3.],[0.,5.],[4.5,5.5],[3.,6.],[7.,6.5],[0.5,2.],[1.5,2.],[2.5,1.],[4.5,3.5],[6.5,3.],[7.,5.5],[3.5,0.5],[2.5,2.],[4.5,1.5],[5.,2.5],[6.,4.],[2.5,3.5],[1.,4.],[2.,6.5],[4.,5.5]])
t_target = array([1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1])

def learnKernelPerceptron(data, target, kernel, h):
	boucle = 0
	alpha = zeros(len(target))
	compt = len(target)
	
	G = computeGram(data, kernel, h)

	while compt > 0 :
		boucle = boucle + 1
		compt = len(target)
		for i in range(len(target)):
			somme = 0
			for j in range(len(target)):
				somme = somme + alpha[j] * target[j] * G[j][i]
	
			if (target[i] * somme) <= 0 :
				alpha[i] = alpha[i] + 1
			else :
				compt = compt - 1

		if boucle > 5000:
			print "Echec lors de l'apprentissage"
			return alpha, True
			
	return alpha, False

def predictKernelPerceptron(alpha, data, target, x, kernel, h):
	somme = 0
	
	for i in range(len(alpha)):
		somme = somme + alpha[i] * target[i] * kernel(x, data[i], h)
		
	if somme < 0:
		return -1
	return 1

def calculeErreur(d_train, t_train, d_test, t_test, kernel, h):
	erreur = 0.

	alpha, echec = learnKernelPerceptron(d_train, t_train, kernel, h)

	for i in range(len(d_test)):
		prediction = predictKernelPerceptron(alpha, d_train, t_train, d_test[i], kernel, h)
		if prediction != t_test[i]:
			erreur = erreur + 1.
	erreur = erreur / len(d_test)

	if echec: 
		erreur += 1.0

	return erreur

def bestHyperparametre(data, target, kernel):
	h = 1
	erreur_min = 1.0
	err = ones(10)

	d_train, d_test, t_train, t_test = cross_validation.train_test_split(data, target, test_size=0.25)

	for i in range(0,10):
		err[i] = calculeErreur(d_train, t_train, d_test, t_test, kernel, i+1)
		if err[i] < erreur_min:
			erreur_min = err[i]
			h = i+1
            
	return (h, err)
	
"""	
kernel = noyauGaussien
#kernel = noyauPolynomial

h, err = bestHyperparametre(t_sample, t_target, kernel)
print "Erreurs :"
print err
print "Best hyperparameter =", h
"""
