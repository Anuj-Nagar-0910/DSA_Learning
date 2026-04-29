'''
Get two matrices and add them.  
'''

def addition_of_matrix(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]


if __name__ == "__main__":
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8, 9], [10, 11, 12]]
    result = addition_of_matrix(mat1, mat2)
    print("Matrix 1:", mat1)
    print("Matrix 2:", mat2)
    print("Sum:", result)
