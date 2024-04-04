# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 03:12:38 2024

@author: Jahna
"""
import matplotlib.pyplot as plt

def harmonic_numbers(n):
    harmonic_sum = 0
    for i in range(1, n + 1):
        harmonic_sum += 1 / i
    
    return harmonic_sum

def average_length(n):
    
    return (2 * n) / (2* harmonic_numbers(2*n) - harmonic_numbers(n))

def average_number(n):
    
    return harmonic_numbers(2*n) - (1/2) * harmonic_numbers(n)


n = 10000
#print(harmonic_numbers(n))

values = []
x_vals = []

for i in range(1,n+1):
    x_vals.append(i)
    values.append(average_length(i))
    
    
plt.plot(x_vals, values)
plt.xlabel('values of n')
plt.ylabel('average length of loop')
plt.title("relationship between the average length of a loop in the bowl after the final knot and n")
plt.show()
    

values = []
x_vals = []

for i in range(1,n+1):
    x_vals.append(i)
    values.append(average_number(i))
    
    
plt.plot(x_vals, values)
plt.xlabel('values of n')
plt.ylabel('average number of loops')
plt.title("relationship between the average number of loops in the bowl after the final knot and n")
plt.show()
    