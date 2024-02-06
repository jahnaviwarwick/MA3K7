# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:55:07 2024

@author: Jahna
"""
from scipy import linalg


def count(matrix):
    num_zeroes = 0
    num_ones = 0
    for row in matrix:
        for cell in row:
            if cell == 0:
                num_zeroes += 1
            else:
                num_ones += 1
            
    return (num_zeroes - num_ones)
    

def generate_matrices(n):
    def generate_helper(matrix, row, col):
        if row == n:
            if 0 <= count(matrix) <= 1:
                matrices.append([list(row) for row in matrix])
            return
            
    

        for value in [0, 1]:
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
    
n = 3
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


print("matrices with determinant 0 but no zero line look like: ")

has_0_line = 0
has_no_0_line = 0
for matrix in matrices_nxn:
    if linalg.det(matrix) == 0:
        if has_zero_sum(matrix) == 1:
            has_0_line += 1
        else: 
            has_no_0_line += 1
            print_m(matrix)

print("of the matrices with det 0, the number of matrices with a line of zeros: " +str(has_0_line))
print("and those without a line of zeroes: " +str(has_no_0_line))
print("________________________________")


'''
        
print("the valid matrices of dimension " + str(n)+" with determinant not 0 look like: ")

num_of_matrices = len(matrices_nxn)
det_n0 = 0
for matrix in matrices_nxn:
    if linalg.det(matrix) != 0:
        det_n0 += 1
        print_m(matrix)

print(det_n0)
print("________________________________")

'''