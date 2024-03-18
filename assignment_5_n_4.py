# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:21:36 2024

@author: Jahna
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:32:47 2024

@author: Jahna
"""
from functools import reduce
import numpy as np
from itertools import permutations
import itertools

def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)

def find_disjoint(result):
    valid_matrices = []
    for a in result:
        valid = [a]
        
        for b in result:
            if not bool(set(b) & set(reduce(lambda z, y :z + y, valid))):
                valid.append(b)
                

        valid = (sorted(valid, key=lambda x: x[0]))
        if len(valid) == n and valid not in valid_matrices:
            valid_matrices.append(valid)
            
                
  
    return valid_matrices

def row_sum_prop(start, target, combination, combinations):
        if target == 0 and len(combination) == n:
            combinations.append(combination)
            return
        if target < 0 or len(combination) >= n:
            return

        for i in range(start, n * n + 1):
            if i > target:
                break
            row_sum_prop(i + 1, target - i, combination + [i], combinations)

def find_combinations(n, target_sum):

    combinations = []
    row_sum_prop(1, target_sum, [],combinations)
    
    return combinations
    '''
    all_matrices = []
    for matrix in combinations:

        perms = (list(permutations(matrix)))
        if not bool(set(perms) & set(all_matrices)):
            all_matrices += (perms)
        
    #all_matrices = [list(t) for t in all_matrices]
    
    return all_matrices
'''
def filter_6_and_11(result):
    final = result.copy()
    for matrix in result:
        if [7,8,9,10] in matrix:
            if find(6, matrix)[0] != find(11, matrix)[0]:
                final.remove(matrix)
    return final

def filter_alternate(result):
    final = result.copy()
    for matrix in result:
        for row in matrix:
            diff = np.diff(row)

            if bool(set(diff) & {2}): 
                final.remove(matrix)
                break
           
    return final

                
                
n = 4
target_sum = int(n*(n**2 +1)/2)
result = find_combinations(n, target_sum)
print("Combinations that sum up to", target_sum, "are:")
print(result)


#valid_matrices = findsubsets(result,n)
valid_matrices = find_disjoint(result)


print("Disjoint combinations of size "+ str(n) +":")
    
for matrix in valid_matrices:
    print(matrix)

print("Filtered combinations of size "+ str(n) +":")

filtered = filter_alternate(valid_matrices)
for matrix in filtered:
    print(matrix)
    
'''
print("2nd Filtered combinations of size "+ str(n) +":")

filtered_2 = filter_6_and_11(filtered)
for matrix in filtered_2:
    print(matrix)
    '''