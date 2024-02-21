# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:30:00 2024

@author: Jahna
"""
import random

n= 50
repeat = 1000
table= []

#for j in range (1,n+1):
for j in [1,2,3,4,5]:
    final_nos = []

    for i in range(repeat):
        papers = [i for i in range(1,j+1)]
    
        while len(papers) != 1:
            
            a  , b= random.sample(papers, 2)
            diff = abs(a - b) #for extension: diff = a - b
            papers.remove(a)
            papers.remove(b)
            papers.append(diff)
        final_no = papers[0]
    
        if final_no not in final_nos:
            final_nos.append(final_no)
            final_nos.sort()
            
    sum1= j*(j+1)//2

    table.append([j,final_nos])

    
for i in table: 
    print(i)
    
    
