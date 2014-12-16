# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:46:35 2012

@author: thomaspeel
"""

from numpy import load

def importImageVect():
	return load("images.npy")
	
def importImageHist():
	return load("histograms.npy")
