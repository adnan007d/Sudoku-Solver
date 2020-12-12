class Sudoku:

    def __init__(self,n):
        self.n = n


    def check(self,i,j,x):
        for z in range(9):
            if self.n[i][z] == x:
                return False
        for z in range(9):
            if self.n[z][j] == x:
                return False
        r =(i//3)*3
        c =(j//3)*3
        for h in range(3):
            for k in range(3):
                if self.n[r+h][c+k] == x:
                    return False
        return True

    def final_solve(self):
        for i in range(9):
            for j in range(9):
                if self.n[i][j] == 0:
                    for x in range(1,10):
                        if self.check(i,j,x):
                            self.n[i][j] = x
                            if self.final_solve():
                                return True
                            self.n[i][j] = 0
                    return False
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.n[i][j] != 0:
                    temp = [self.n[k][i] for k in range(9)]
                    if self.n[i].count(self.n[i][j]) > 1 or temp.count(self.n[i][j]) > 1:
                        return False
                    r = (i//3)*3
                    c = (i//3)*3
                    temp = [self.n[h+r][u+c] for h in range(3) for u in range(3)]
                    if temp.count(self.n[i][j]) > 1:
                        return False
            
        if self.final_solve():
            return True
        else:
            return False