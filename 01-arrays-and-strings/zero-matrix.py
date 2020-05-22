'''
Write an algorithm such that if an element in an M x N matrix is 0, 
its entire row and column are set to 0.
'''
'''
start a new matrix copying the input
loop through coordinates
    if 0 coord
    loop through length of row and set to 0
    loop through # of rows at the column and set to 0 in new matrix
return new matrix
'''

'''
. . . . .
. . 0 . .
. . . . .

. . 0 . .
0 0 0 0 0
. . 0 . .
'''

def zero_matrix(matrix):
    result = [row.copy() for row in matrix]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                for i in range(len(matrix[0])):
                    result[r][i] = 0
                for j in range(len(matrix)):
                    result[j][c] = 0
    return result

matrix = [
    [1,1,1,1],
    [1,1,1,1],
    [1,0,1,1],
]
print(zero_matrix(matrix))