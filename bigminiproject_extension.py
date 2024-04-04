# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:47:13 2024

@author: Jahna
"""

import networkx as nx
import matplotlib.pyplot as plt
import random



def simulate_string_loops(num_strings, num_ties):

    G = nx.Graph()
    strings = [i for i in range(1,num_strings+1)]

    G.add_nodes_from(strings)
    i = 0

    for _ in range(num_ties):
        if i % 10 == 0:
           visualise_graph(G,num_strings,i)
        #visualise_graph(G,num_strings,i)
            
        i+=1 
    
        u = random.choice(strings)
        if G.degree(u) == 1:
            strings.remove(u)
            
        v = random.choice(strings)
        if u!= v and G.degree(v) == 1:
            strings.remove(v)
        elif u == v:
            strings.remove(v)
        
        G.add_edge(u,v)
        
        
        
        
        
    return G

def visualise_graph(G,n,t):

    plt.figure(figsize=(4,3))
    nx.draw(G, with_labels=True, node_size=100, font_size=10, node_color='skyblue')
    plt.title("Simulated String Loops when n = "+str(n)+" and you've tied "+ str(t)+" knots")
    plt.show()
    
   


num_strings = 50
num_ties = num_strings

string_loops_graph = simulate_string_loops(num_strings, num_ties)

visualise_graph(string_loops_graph,num_strings,num_ties)