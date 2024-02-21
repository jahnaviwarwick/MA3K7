# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:59:51 2024

@author: Jahna
"""

import matplotlib.pyplot as plt
import random

n= 25
final_nos = {}
repeat = 10000
m=1
final = []

for j in [2024]:
    for i in range(repeat):
        papers = [i for i in range(1,j+1)]
    
        while len(papers) != 1:
            
            a  , b= random.sample(papers, 2)
            diff = abs(a - b)
            papers.remove(a)
            papers.remove(b)
            papers.append(diff)
        
        final_no = papers[0]
        if final_no not in final_nos.keys():
            final_nos[final_no]  = 1
        else:
            final_nos[final_no] += 1
        
        if final_no not in final:
              final.append(final_no)
              final.sort()
      
    '''
    plt.subplot(2,2,m)
    x = final_nos.keys()
    y = final_nos.values()
    if m  == 1 or m == 3:
        plt.ylabel("frequency")
    if m == 3 or m == 4:
        plt.xlabel("possible final numbers")
     
    plt.bar(x,y)
    m+=1
    '''

#print(final_nos)
x = final_nos.keys()
y = final_nos.values()
plt.ylabel("frequency")
plt.xlabel("possible final numbers")
plt.bar(x,y)
print(final)

    
    