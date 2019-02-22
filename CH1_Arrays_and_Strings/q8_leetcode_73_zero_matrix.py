# try with O(1) extra space

def zero_matrix(matrix):
    print(matrix)

    length = len(matrix)
    width = 0

    indices = set()
    if length > 0:
        width = len(matrix[0])

    for i in range(length):
        for j in range(width):
            if matrix[i][j] == 0:
                indices.add((i,j))

    for point in indices:
        for i in range(width):
            matrix[point[0]][i] = 0
        for j in range(length):
            matrix[j][point[1]] = 0

    for row in matrix:
        print(row)

matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

zero_matrix(matrix)