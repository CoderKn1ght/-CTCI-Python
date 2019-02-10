def number_of_unique_ways(m,n):
    list = [[1 for x in range(m)] for y in range(n)]

    for i in range(1,n):
        for j in range(1,m):
            list[i][j] = list[i][j-1] + list[i-1][j]

    return list[n-1][m-1]

def same_as_above_but_without_initializing_first_values_to_1(m,n):
    grid = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                grid[i][j] = 1
                continue
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[n-1][m-1]

print(same_as_above_but_without_initializing_first_values_to_1(7,3))