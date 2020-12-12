#ifndef SUDOKU_H
#define SUDOKU_H

class Sudoku
{
    private:
    int (*a)[9]; // 2d array to store and return the solved array
    public:
    Sudoku()
    {

    }
    Sudoku(int n[9][9])
    {
        a = n;
    }

    bool check(int i ,int j, int x)
    {
        for (int u=0;u<9;u++)
            if (a[i][u] == x)
                return false;

        for (int v=0;v<9;v++)
            if (a[v][j] == x)
                return false;

        int h = (i/3)*3;
        int k = (j/3)*3;

        for (int u=0;u<3;u++)
            for (int v=0;v<3;v++)
                if (a[h+u][k+v] == x)
                    return false;
        return true;
    }


    bool final_solve ()
    {

        for (int i=0;i<9;i++)
        {
            for (int j=0;j<9;j++)
            {
                if (a[i][j] == 0)
                {
                    for(int k=1;k<=9;k++)
                    {
                        if (check(i,j,k))
                        {
                            a[i][j] = k;
                            if ( solve() )
                                return true;
                        }
                        a[i][j] = 0;
                    }
                    return false;
                }
            }
        }
        return true;
    }

    bool solve()
    {
        for (int i=0;i<9;i++)
            for (int j=0;j<9;j++)
                if (a[i][j] != 0)
                {
                    int max = 0;
                    for (int k=0;k<9;k++)
                        if (a[i][k] == a[i][j])
                            max += 1;
                    if (max>1)
                        return false;
                    max = 0;
                    for (int k=0;k<9;k++)
                        if (a[k][j] == a[i][j])
                            max += 1;
                    if (max>1)
                        return false;
                    int r = (i/3)*3;
                    int c = (j/3)*3;
                    max = 0;
                    for (int h=0;h<3;h++)
                        for (int k=0;k<3;k++)
                            if (a[h+r][k+c] == a[i][j])
                                max += 1;
                    if (max>1)
                        return false;
                }

        if (final_solve())
            return true;
        else
            return false;
    }

};
#endif // SUDOKU_H
