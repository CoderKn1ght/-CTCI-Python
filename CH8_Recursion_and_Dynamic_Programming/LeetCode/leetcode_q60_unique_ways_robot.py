def number_of_unique_ways(m,n):
    list = [[1 for x in range(m)] for y in range(n)]

    for i in range(1,n):
        for j in range(1,m):
            list[i][j] = list[i][j-1] + list[i-1][j]

    return list[n-1][m-1]

print(number_of_unique_ways(7,3))