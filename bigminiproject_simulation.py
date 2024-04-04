# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:50:28 2024

@author: Jahna
"""

import random



def find_chain(chain, to_find):
    for sublist in chain:
        if to_find in sublist:
            return chain.index(sublist)

def tying_two_ends(n,t):

    loops = []
    chains = [[i] for i in range(1,n+1)]

    
    ends = []
    print("chains at t=0: " + str(chains))
    print('loops at t=0: ' + str(loops))
    for i in range(1,n+1):
        ends.append(str(i)+"A")
        ends.append(str(i)+"B")
        
    for i in range(1,t+1):
       if  len(chains)==0:
           loops.append(chains)
           ends = []
           break
                         
       end_1, end_2 = random.sample(ends,2)
       print(end_1)
       print(end_2)
       end_1_chain_index= find_chain(chains,int(end_1[:-1])) 
       end_2_chain_index= find_chain(chains,int(end_2[:-1]))
       end_1_chain = chains[end_1_chain_index]
       end_2_chain = chains[end_2_chain_index]
       if end_1_chain_index == end_2_chain_index:
           loops.append(end_1_chain)
           chains.remove(end_1_chain)
       else:
           new_chain= end_1_chain+(end_2_chain)
           chains.append(new_chain)
           chains.remove(end_1_chain)
           chains.remove(end_2_chain)
           
       ends.remove(end_1)
       ends.remove(end_2)


       print("chains at t= " + str(i)+": " + str(chains))
       print("loops at t= " + str(i)+": " + str(loops))
       
       
    


n = 4
t = n
tying_two_ends(n,t)

