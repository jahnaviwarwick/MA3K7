import itertools

def find(element, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == element:
                return (i, j)
            
def is_consecutive_adjacent(matrix,n):
    indices = []
    for i in range(1,n**2+1):
        indices.append(find(i,matrix))
        
    for i in range(1,n**2):
        a = indices[i-1]
        b = indices[i]
        if abs(a[0]-b[0]) == 0 and abs(a[1]-b[1]) == 1 or abs(a[1]-b[1]) == 0 and abs(a[0]-b[0]) == 1:
            continue
        else:
            return False
    
    return True
        

def check_row_sums(matrix,n):

    row_sums = [sum(matrix[i]) for i in range(n)]
    return all(row_sums[i] == row_sums[0] for i in range(1, n))

def check_column_sums(matrix,n):
    column_sums = [sum([j[i] for j in matrix]) for i in range(n)]
    return all(column_sums[i] == column_sums[0] for i in range(1, n))

def generate_matrices(n):
    values = list(range(1, n**2 + 1))
    
    permutations = list(itertools.permutations(values, n**2))
    

    matrices = []
    for perm in permutations:
        matrix = [list(perm[i:i+n]) for i in range(0, n**2, n)]
        if check_row_sums(matrix,n) and is_consecutive_adjacent(matrix,n):# and check_column_sums(matrix,n):# and is_consecutive_adjacent(matrix,n):

            matrices.append(matrix)
        
    
    return matrices

n = 2
all_matrices = generate_matrices(n)

print('The matrices with the rows-sum and consecutive adjacency property for n = ' + str(n)+":")
for i, matrix in enumerate(all_matrices):
    print(f"Matrix {i+1}:")
    for row in matrix:
        print(row)
    print()


print('The matrices with the rows-sum, column-sum and consecutive adjacency property for n = ' + str(n)+":")
for i, matrix in enumerate(all_matrices):
    if check_column_sums(matrix,n):
        print(f"Matrix {i+1}:")
        for row in matrix:
            print(row)
            print() 