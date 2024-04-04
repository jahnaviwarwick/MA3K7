# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:50:28 2024

@author: Jahna
"""

import random
import matplotlib.pyplot as plt
import collections


def find_amount(array):
    total_elements = 0
    for subarray in array:
        total_elements += len(subarray)

    return (total_elements)


def find_chain(chain, to_find):
    for sublist in chain:
        if to_find in sublist:
            return chain.index(sublist)

def tying_two_ends(n,t):

    loops = []
    chains = [[i] for i in range(1,n+1)]

    
    ends = []
    #print("chains at t=0: " + str(chains))
    #print('loops at t=0: ' + str(loops))
    for i in range(1,n+1):
        ends.append(str(i)+"A")
        ends.append(str(i)+"B")
        
    for i in range(1,t+1):
       if  len(chains)==0:
           loops.append(chains)
           ends = []
           break
                         
       end_1, end_2 = random.sample(ends,2)
       #print(end_1)
       #print(end_2)
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


       #print("chains at t= " + str(i)+": " + str(chains))
       #print("loops at t= " + str(i)+": " + str(loops))
       
    return loops, chains

######################################################################################################       
    
def frequencies(num_of_strings_in_chains, num_of_strings_in_loops):
    freqs_chains = collections.Counter(num_of_strings_in_chains)
    freqs_loops = collections.Counter(num_of_strings_in_loops)

    #print(freqs_chains)
    #print(freqs_loops)

    props_chains= []
    props_loops =[]


    for (key, value) in freqs_chains.items():
        props_chains.append([int(key), int(value)/x])
        
    for (key, value) in freqs_loops.items():
        props_loops.append([int(key), int(value)/x])
        
        
    #print(props_chains)
    #print(props_loops)
    props_chains = sorted(props_chains, key=lambda x: x[0])
    
    props_loops = sorted(props_loops, key=lambda x: x[0])
    
    return props_chains, props_loops
 ##################################################################################################   


n = 2
#ts = [1,15,25,40,49,50]
ts = [0,1,2]
#tying_two_ends(n,t)
avgs_chains = []
avgs_loops = []

no_of_loops = []
pos = 1

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

for t in ts:
    x = 10000
    
    num_of_strings_in_chains=[]
    num_of_strings_in_loops=[]
    
    for j in range(1,x+1):
        loops, chains = tying_two_ends(n,t)
    
        num_of_strings_in_chains.append(find_amount(chains))
        num_of_strings_in_loops.append(find_amount(loops))
        
        
    

    x_values = [i for i in range(0,n+1)]
    
    proportions_of_chains, proportions_of_loops = frequencies(num_of_strings_in_chains, num_of_strings_in_loops)

   
    plt.subplot(2, 3, pos)
    plt.plot([i[0] for i in proportions_of_chains],[i[1] for i in proportions_of_chains], marker = 'o', label = 'chains')
    plt.plot([i[0] for i in proportions_of_loops], [i[1] for i in proportions_of_loops], marker = 'o', label = 'loops')
    print([i[1] for i in proportions_of_chains])
    plt.xlabel("possible values of x")
    plt.ylabel("probabilities")
    plt.title("t = "+str(t))
    plt.xticks(x_values)
    plt.ylim(0,1.1)
 
    pos += 1
 
  
    
fig.tight_layout()

plt.suptitle('the probability that the number of strings in chains/loops is x for different values of t when n = '+str(n), y = 1)

plt.legend()
plt.show()
    