# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 18:04:38 2024

@author: Jahna
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:55:07 2024

@author: Jahna
"""
from scipy import linalg


def count(matrix):
    num_mones = 0
    num_ones = 0
    for row in matrix:
        for cell in row:
            if cell == -1:
                num_mones += 1
            else:
                num_ones += 1
            
    return (num_ones - num_mones)
    

def generate_matrices(n):
    def generate_helper(matrix, row, col):
        if row == n:
            if 0 <= count(matrix) <= 1:
                matrices.append([list(row) for row in matrix])
            return
            
    

        for value in [1, -1]:
            matrix[row][col] = value
            if col < n - 1:
                generate_helper(matrix, row, col + 1)
            else:
                generate_helper(matrix, row + 1, 0)

    matrices = []
    initial_matrix = [[0] * n for _ in range(n)]
    generate_helper(initial_matrix, 0, 0)
    return matrices

def has_zero_sum(matrix):
        for row in matrix:
            if sum(row) == 0:
                return 1
        for col in zip(*matrix):
            if sum(col) == 0:
                return 1
        return 0


def print_m(matrix):
    for row in matrix:
        print(row)
    print()
    
n = 2
matrices_nxn = generate_matrices(n)

print("the valid matrices of dimension " + str(n)+" with determinant 0 look like: ")

num_of_matrices = len(matrices_nxn)
det_0 = 0
for matrix in matrices_nxn:
    if linalg.det(matrix) == 0:
        det_0 += 1
        print_m(matrix)

        
print("the number of valid matrices are: "+ str(num_of_matrices))
print("the number of these matrices with determinant zero are: "+str(det_0))
print("________________________________")

