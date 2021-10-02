'''
You are given a rectangular matrix of characters matrix, which represents a 2-dimensional field where each cell is either empty ('.'), contains an obstacle (#), or corresponds to a cell of a connected figure ('F').
Gravity makes the figure fall through the field, until one of its cells reaches the ground, or meets an obstacle. Your task is to return the state of the field after the figure has fallen.
Note that it is guaranteed that the figure is connected, ie. between any two cells of the figure there exists a path which goes through the cells' sides (not through corners).

For example:
F F F       . . .
. F .       . . .
. F F       F F F
# F .  ==>  # F .
F F .       . F F
. . .       . F .
. . #       F F #
. . .       . . .
'''
from typing import MutableSet


def figureUnderGravity(matrix):
    if not matrix or not matrix[0]:
        return matrix
    m, n = len(matrix), len(matrix[0])
    minstep = float('inf')

    # first we need to find the min step that the whole figure will fall
    for j in range(n):
        i = 0
        while i < m:
            # find where the first F show in every col
            while i < m and matrix[i][j] != 'F':
                i += 1
            if i == m:
                continue
            
            # find the last F in the current column
            while i < m and matrix[i][j] == 'F':
                i += 1
            if i < m:
                cnt = 0
                # find the min step that the above Fs can fall
                while i < m and matrix[i][j] != '#':
                    i += 1
                    cnt += 1
                minstep = min(minstep, cnt)
    # edge cases
    if minstep == float('inf') or minstep == 0:
        return matrix
    
    for i in range(m-1, minstep-1, -1):
        for j in range(n):
            if matrix[i-minstep][j] == 'F':
                matrix[i][j] = 'F'
                matrix[i-minstep][j] = '.'
    return matrix 

if __name__ == "__main__":
    matrix = [
["F", "F", "F"],
[".", "F", "."],
[".", "F", "F"],
["#", "F", "."],
["F", "F", "."],
[".", ".", "."],
[".", ".", "#"],
[".", ".", "."]
]

    expected = [
[".", ".", "."],
[".", ".", "."],
["F", "F", "F"],
["#", "F", "."],
[".", "F", "F"],
[".", "F", "."],
["F", "F", "#"],
[".", ".", "."]
]

    if figureUnderGravity(matrix) == expected:
        print('pass')
    else:
        print('not pass')