# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 00:06:19 2020

@author: sandhya
"""

import numpy as np
from numpy import linalg 

#Define the matrices M( matrix of normal vectors) & b(point on the plane)
M = np.array([[3,3],[-2,2],[-1,-1]])
b = np.array([[1],[-.5],[3]])


#Singular Value Decomposition of M
U, s, V = linalg.svd(M)
#print('U & s & V matrices are: ')
#print('U = {} s = {} V ={}'.format(U,s, V))

#Find Moore Penrose Pseudo Inverse of matrix s
S = np.zeros(M.shape)
Splus = S.T
S[:2,:2] = np.diag(s)
#Reciprocal of s
sinv = 1./s
Splus[:2,:2] = np.diag(sinv)
#print(Splus)

#Solution
x = V.T.dot(Splus).dot(U.T).dot(b)
print('Solution for foot of the perpendicular is {}'.format(x))




