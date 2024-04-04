# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:24:18 2024

@author: Jahna
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:50:28 2024

@author: Jahna
"""

import random
import matplotlib.pyplot as plt
import collections

############################################################################################
def init(n,t):
    output = 1
    for i in range(1,t+1):
        term = 2*(n-i)/(2*(n-i)+1)
        output = output * term
    return output

def p(x, t, n):
    if x == 0 and t == 0:
        return 1
    elif t == 0:
        return 0
    elif x == 0: 
        return init(n,t)

    else:
        return p(x-1, t-1, n) / (2*(n-t)+1) + 2*(n-t)*p(x, t-1, n) / (2*(n-t)+1)
    
    
    
def average_no_of_loops(n,t):
        probs = []
        for x in range(0,t+1):
            result = p(x, t, n)
            probs.append([x,result])
                       
        return find_average(probs) 
         


def find_average(proportions):
    avg = 0

    for i in proportions:
        avg += i[0]*i[1]
        
    return avg


def find_average_no_of(n,t,array,no_of_loops,chains = True):
    chain = n-t
    loop = no_of_loops[find_chain(no_of_loops,t)][1]
    
    if chains:
        if chain ==0: return 0
        else: return find_average(array)/chain
    else:
        if loop ==0: return 0
        else: return find_average(array)/loop
    
##############################################################################################
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
######################################################################################################       

    
def plot_averages(avgs,ts):
    plt.plot(ts, avgs, marker = 'o')
    plt.xticks((ts))
    plt.xlabel('values of t')
    plt.ylabel('length of chains')
    plt.title("average length of a chain in the bowl after t knots when n = "  + str(n))
    plt.legend()
    plt.show()
    
'''      
def plot_averages(avgs_chains,avgs_loops,ts):
    plt.plot(ts, avgs_chains, label = 'average length of chains', marker = 'o')
    plt.plot(ts, avgs_loops, label = 'average length of loop', marker = 'o')
    plt.xticks((ts))
    plt.xlabel('values of t')
    plt.ylabel('length of chains/loops')
    plt.title("average length of a chain/loop in the bowl after t knots when n = "  + str(n))
    plt.legend()
    plt.show()
'''

####################################################################################################
n = 2
#ts = [1,15,25,40,49,50]
ts = [0,1,2]
#tying_two_ends(n,t)
avgs_chains = []
avgs_loops = []

no_of_loops = []
pos = 1
for t in ts:
    no_of_loops.append([t,average_no_of_loops(n,t)])
    

for t in ts:
    x = 100000
    
    num_of_strings_in_chains=[]
    num_of_strings_in_loops=[]
    
    for j in range(1,x+1):
        loops, chains = tying_two_ends(n,t)
    
        num_of_strings_in_chains.append(find_amount(chains))
        num_of_strings_in_loops.append(find_amount(loops))
        
        
    
    x_values = [i for i in range(0,n+1)]
    
    proportions_of_chains, proportions_of_loops = frequencies(num_of_strings_in_chains, num_of_strings_in_loops)
    
 
    avgs_chains.append(find_average_no_of(n,t,proportions_of_chains,no_of_loops,chains = True))
    avgs_loops.append(find_average_no_of(n,t,proportions_of_loops,no_of_loops, chains = False))
    

print(avgs_chains)
print(avgs_loops)
plot_averages(avgs_chains,ts)
plot_averages(avgs_loops,ts)
