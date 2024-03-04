# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:56:07 2024

@author: Jahna
"""
import matplotlib.pyplot as plt


def recursive_function(p_1,p_2, k):
    p_n_1 = p_2
    p_n_2 = p_1

    for i in range(3,k+1):
       p_n = (p_n_1 + p_n_2) / 2
       p_n_2 = p_n_1
       p_n_1 = p_n
    
    return p_n

def recursive_function1(p_1,p_2, k):
    p_n_1 = p_2
    p_n_2 = p_1

    for i in range(3,k+1):
       p_n = (p_n_1 + p_n_2) / 2
       p_n_2 = p_n_1
       p_n_1 = p_n
    
    return p_n

n = 13

#plotting the probabilities for a range of ns
m=50
x = [i for i in range(3,m)]
y = []
p_1 = 1
p_2 = 0.5
for i in range(3,m):
    y.append(recursive_function(p_1, p_2, i))

plt.plot(x,y)



