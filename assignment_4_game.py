# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 17:14:50 2024

@author: Jahna
"""
import random


def game(step,n):

    
    while step <= n-1:
        step += random.randint(1,2)

        
    if step == n:
        return 1
    else:
        return 0
        
step = 1
success = 0
n = 25

k = 100000

for i in range(1,k+1):
    success += game(step,n)

print("The exercise was simulated " + str(k) +" times and there were "+ str(success) + " successes.")