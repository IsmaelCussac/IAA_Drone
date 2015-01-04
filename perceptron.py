import math 
from numpy import *
from noyau import *
from sklearn import cross_validation

sample = array([[3.5,0.5],[2.5,2.],[4.5,1.5],[5.,2.5],[6.,4.],[2.5,3.5],[1.,4.],[2.,6.5],[4.,5.5]])
target = array([-1,-1,-1,-1,-1,1,1,1,1])

t_sample= array([[2.,3.],[0.,5.],[4.5,5.5],[3.,6.],[7.,6.5],[0.5,2.],[1.5,2.],[2.5,1.],[4.5,3.5],[6.5,3.],[7.,5.5],[3.5,0.5],[2.5,2.],[4.5,1.5],[5.,2.5],[6.,4.],[2.5,3.5],[1.,4.],[2.,6.5],[4.,5.5]])
t_target = array([1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1,1,1])

#Fonction d'apprentissage d'un echantillon de donnees.
#Retourne un perceptron a noyau appris sur les donnees grace au noyau et son parametre
def learnKernelPerceptron(data, target, kernel, h, max_boucle = 5000):
	boucle = 0
	alpha = zeros(len(target))
	compt = len(target)

	G = computeGram(data, kernel, h)

	while compt > 0 :
		boucle = boucle + 1
		compt = len(target)
		for i in range(len(target)):
			somme = 0.
			for j in range(len(target)):
				somme = somme + alpha[j] * target[j] * G[j][i]
					
			if (target[i] * somme) <= 0 :
				alpha[i] = alpha[i] + 1
			else :
				compt = compt - 1
				
		if boucle > max_boucle:
			print "Echec lors de l'apprentissage"
			return alpha, True
	
	return alpha, False

#Predit la classe d'un exemple
def predictKernelPerceptron(alpha, data, target, x, kernel, h):
	somme = 0.0
	
	for i in range(len(alpha)):
		somme = somme + alpha[i] * target[i] * kernel(x, data[i], h)
		
	if somme < 0:
		return -1
	return 1

#Retourne l'erreur de prediction
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

#Retourne la valeur de l'hyperparametre de la fonction noyau demandee
def bestHyperparametre(data, target, kernel):
	h = 1.0
	erreur_min = 1.0
	err = ones(10)

	d_train, d_test, t_train, t_test = cross_validation.train_test_split(data, target, test_size=0.10)
	
	if kernel == noyauGaussien :
		loop = 20
		coef = 10**3
		err = ones(loop)
		
	else :
		loop = 10
		coef = 1.
		err = ones(loop)
		
	for i in range(0,loop):
		print "Test avec",(i+1)*coef
		err[i] = calculeErreur(d_train, t_train, d_test, t_test, kernel, (i+1)*coef)
		if err[i] < erreur_min:
			erreur_min = err[i]
			h = (i+1)*coef

	return (h, err)
	
	
if __name__ == '__main__':
	kernel = noyauPolynomial
	k = input("Choix du kernel (1-Gaussien / 2-Polynomial): ")
	if k == 1 :
		kernel = noyauGaussien

	h, err = bestHyperparametre(t_sample, t_target, kernel)
	print "Erreurs :"
	print err
	print "Best hyperparametre =", h

