size = 0
newmatrix = []
def rotate_matrix(matrix, degrees):
    global size, newmatrix
    if(degrees>0):
        size=len(matrix)
        newmatrix = [[0] * size for _ in range(size)]
        for r in range(0,size):
            for c in range(0,size):
                newmatrix[c][size-1-r]=matrix[r][c]
        return rotate_matrix(newmatrix,degrees-90)
    else:
        return(matrix)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result=rotate_matrix(matrix,180)
print(result)
  