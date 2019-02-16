def solve(maze):
    solution_matrix = [[0 for i in range(len(maze))] for j in range(len(maze[0]))]

    for list in maze:
        print(list)

    x = 0
    y = 0

    possible, solution_matrix = solve_util(solution_matrix, maze, x, y)

    print("-------------------------")
    print("possible:", possible)
    for list in solution_matrix:
        print(list)

def solve_util(solution_matrix, maze, x, y):

    solution_matrix[x][y] = 1

    if x == len(maze)-1 and y == len(maze[0])-1:
        return True, solution_matrix

    if x < len(solution_matrix) - 1:
        if maze[x+1][y]:
            decision, solution_matrix = solve_util(solution_matrix,maze,x+1,y)
            if decision:
                return True, solution_matrix

    if y < len(solution_matrix[0])-1:
        if maze[x][y+1]:
            decision, solution_matrix =  solve_util(solution_matrix,maze,x,y+1)
            if decision:
                return True, solution_matrix

    return False, solution_matrix



maze = [[1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,1]
        ]

solve(maze)