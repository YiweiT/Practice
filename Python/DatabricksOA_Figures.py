# https://leetcode.com/discuss/interview-question/842141/Databricks-OA
def almostTetris(n, m, figures):
    grid = [[0] * m for _ in range(n)]

    shapes = {
        1: [(0, 0)],
        2: [(0, 0), (0, 1), (0, 2)],
        3: [(0, 0), (0, 1), (1, 0), (1, 1)],
        4: [(0, 0), (1, 0), (1, 1), (2, 0)],
        5: [(0, 1), (1, 0), (1, 1), (1, 2)]
    }

    def checkShapeFit(x, y, shape_no, number):
        for (i, j) in shapes[shape_no]:
            if x+i >= n or y+j >= m or x+i < 0 or y+j < 0 or grid[x+i][y+j] != 0:
                return False
        
        for i, j in shapes[shape_no]:
            grid[x+i][y+j] = number

        return True
    
    def getAvailable(i, f):
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    if checkShapeFit(row, col, f, i+1):
                        return

    for i, f in enumerate(figures):
        getAvailable(i, f)

    return grid
    


if __name__ == "__main__":
    n, m = 4, 4
    figures = [4, 2, 1, 3]
    expected = [[1, 2, 2, 2],
                [1, 1, 3, 0],
                [1, 4, 4, 0],
                [0, 4, 4, 0]]
    
    res = almostTetris(n, m, figures)
    if res == expected:
        print('pass')
    else:
        print('not pass')
        print('expected: \n', expected)
        print('your result: \n', res)