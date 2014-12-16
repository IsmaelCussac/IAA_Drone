import math 
from numpy import *
from noyau import *

sample = array([[1.,0.],[0.,1.],[1.,1.]])
target = array([1,1,-1])

t_sample= array([[0.,0.],[3.,4.],[2.,0.]])


def learnKernelPerceptron(data, target, kernel, h):
	alpha = zeros(len(target))
	compt = len(target)
	G = computeGram(data, kernel, h)

	while compt > 0 :
		compt = len(target)
		for i in range(len(target)):
			somme = 0
			for j in range(len(target)):
				somme = somme + alpha[j] * target[j] * G[j][i]
	
			if (target[i] * somme) <= 0 :
				alpha[i] = alpha[i] + 1
			else :
				compt = compt - 1
				
	return alpha

def predictKernelPerceptron(kp, data, target, x, kernel, h):
	somme = 0
	if kernel == 1 :
		for i in range(len(kp)):
			somme = somme + kp[i] * target[i] * noyauGaussien(x, data[i], h)
	else :
		for i in range(len(kp)):
			somme = somme + kp[i] * target[i] * noyauPolynomial(x, data[i], h)
	if somme < 0:
		return -1
	return 1
	
alpha = learnKernelPerceptron(sample, target, 0, 1)
for i in range(3):
	print predictKernelPerceptron(alpha, sample, target, t_sample[i], 1, 1)

