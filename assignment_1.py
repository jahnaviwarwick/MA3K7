# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:33:26 2024

@author: Jahna
"""
import matplotlib.pyplot as plt
i = 1
j = 5

chain = [i,j]

for i in range(1,200):
        chain.append((chain[-1]+chain[-2])%10)
        

plt.plot(chain)
plt.show()
        
print(chain)
