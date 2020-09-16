def check(n,i,j,x):
    for z in range(9):
        if n[i][z] == x:
            return False
    for z in range(9):
        if n[z][j] == x:
            return False
    r =(i//3)*3
    c =(j//3)*3
    for h in range(3):
        for k in range(3):
            if n[r+h][c+k] == n:
                return False
    return True
def isZero(n):
    for i in range(9):
        for j in range(9):
            if n[i][j] == 0:
                return False
    return True
def sudoku(n):
    if isZero(n):
        return True
    for i in range(9):
        for j in range(9):
            if n[i][j] == 0:
                for x in range(1,10):
                    if check(n,i,j,x):
                        n[i][j] = x
                        if sudoku(n):
                            return True
                        n[i][j] = 0
                return False
