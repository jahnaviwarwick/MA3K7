# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:29:26 2024

@author: Jahna
"""
#from math import comb

n = 13
#Method 1
def recursive_function(p_1,p_2, k):
    p_n_1 = p_2
    p_n_2 = p_1

    for i in range(3,k+1):
       p_n = (p_n_1 + p_n_2) / 2
       p_n_2 = p_n_1
       p_n_1 = p_n
    
    return p_n

p_1 = 1
p_2 = 0.5

p = recursive_function(p_1, p_2, n)
print("using p_n = (p_n-1 + p_n-2)/2, we get that p_"+str(n)+" = "+ str(p))

#Method 2
def recursive_function_2(p_1, k):
    p_n_1 = p_1

    for i in range(2,k+1):
       p_n = 1 - p_n_1/2
       p_n_1 = p_n
    
    return p_n


p = recursive_function_2(p_1, n)
print("using p_n = 1 - p_n-1/2, we get that p_"+str(n)+" = "+ str(p))

'''
#Method 3
x = 0
for i in range(0,n):
    x += comb(12+i,2*i) * (0.5)**(12+i)

#print(x)
'''
    
