#!python

import numpy as np


def write_matrix(matrix, filename, folder, flag=""):
    n = len(matrix)
    m = len(matrix[0])
    
    with open(f'./{folder}/{filename}', 'w') as file:        
        for i in range(n):
            for j in range(m):
                if flag or flag == 0:
                    file.write(f"{flag} ")

                file.write(f'{i} {j} {matrix[i][j]}')
                if (i != n - 1 or j != m - 1):
                    file.write('\n')


input_folder = './input'
solution_folder = './solution'


if __name__ == '__main__':
    np.random.seed(42)

    n = 10
    m = 5
    matrix1_filename = "matrix1.txt"
    matrix2_filename = "matrix2.txt"
    matrices_multiplied_filename = "matrix1 x matrix2.txt"

    fixed_matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    fixed_matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    random_matrix1 = np.random.rand(n, m)
    random_matrix2 = np.random.rand(m, n)

    matrix1 = random_matrix1
    matrix2 = random_matrix2

    write_matrix(matrix1, matrix1_filename, input_folder, 0)
    write_matrix(matrix2, matrix2_filename, input_folder, 1)
    write_matrix(
        np.dot(np.array(matrix1), np.array(matrix2)),
        matrices_multiplied_filename,
        solution_folder)

    print(f'Done!')