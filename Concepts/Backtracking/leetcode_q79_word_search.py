# Runtime is too slow, try faster algo

def solve(board, word):
    for list in board:
        print(list)

    x = y = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
                index = 1
                visited[i][j] = True
                if solve_util(i,j,board,word,index, visited):
                    return True

    return False

def solve_util(x,y,board,word,index,visited):

    if index == len(word):
        return True

    if x+1 < len(board):
        if board[x+1][y] == word[index] and not visited[x+1][y]:
            visited[x+1][y] = True
            if solve_util(x+1,y,board,word,index+1,visited):
                return True

    if x > 0:
        if board[x-1][y] == word[index] and not visited[x-1][y]:
            visited[x-1][y] = True
            if solve_util(x-1,y,board,word,index+1,visited):
                return True

    if y+1 < len(board[0]):
        if board[x][y+1] == word[index] and not visited[x][y+1]:
            visited[x][y+1] = True
            if solve_util(x,y+1,board,word,index+1,visited):
                return True

    if y > 0:
        if board[x][y-1] == word[index] and not visited[x][y-1]:
            visited[x][y-1] = True
            if solve_util(x,y-1,board,word,index+1,visited):
                return True

    visited[x][y] = False
    return False


board =[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]

word = "ABCESEEEFS"

print(solve(board, word))