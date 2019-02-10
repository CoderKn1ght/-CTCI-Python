def number_of_unique_ways_with_obstacles():
    obstacleGrid = [[0,0,1,0,0,0,0],
                    [0,0,0,1,0,0,0],
                    [0,1,1,0,0,0,0]]
    m = len(obstacleGrid[0])
    n = len(obstacleGrid)

    if obstacleGrid[0][0] == 1:
        return 0

    value = 1
    for i in range(1,m):
        if obstacleGrid[0][i] == 0:
            obstacleGrid[0][i] = value
        else:
            value = 0
            obstacleGrid[0][i] = 0

    value = 1
    for i in range(0, n):
        if obstacleGrid[i][0] == 0:
            obstacleGrid[i][0] = value
        else:
            value = 0
            obstacleGrid[i][0] = 0

    for i in range(1,n):
        for j in range(1,m):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                continue
            obstacleGrid[i][j] = 0

    return obstacleGrid[n-1][m-1]

print(number_of_unique_ways_with_obstacles())