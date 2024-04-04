# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:09:58 2024

@author: Jahna
"""
import matplotlib.pyplot as plt



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

n = 20
#x = 0
#t = 3

#result = p(x, t, n)
#print(f"p({x}, {t}) = {result}")



for t in range(1,n+1):
    probs = []
    x_values= []
    for x in range(0,t+1):
        x_values.append(x)
        result = p(x, t, n)
        probs.append(result)
    plt.plot(x_values,probs,label = "after " + str(t) + " knots", marker = 'o')
    #plt.plot(x_values,probs,marker = 'o')
 
print(probs)

plt.xticks(x_values)
plt.xlabel("x")
plt.ylabel("probability that l(n,t) = x")
plt.title('the probability that the l('+str(n)+',t) = x at different t')
plt.legend()
#plt.xlabel()
plt.show()

for x in range(0,n+1):
    probs = []
    x_values= []
    for t in range(1,n+1):
        x_values.append(t)
        result = p(x, t, n)
        probs.append(result)
    plt.plot(x_values,probs,label = ("x = " + str(x)), marker = 'o')
    #plt.plot(x_values,probs,marker = 'o')
 
print(probs)

plt.xticks(x_values)
plt.xlabel("t")
plt.ylabel("probability that l(n,t) = x")
plt.title('the probability that the l('+str(n)+',t) = x at different x')
plt.legend()
#plt.xlabel()
plt.show()