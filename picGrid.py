'''
Created on Jul 20, 2017

@author: ahmed
test for using loop within loops
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def picGrid(grid):
    x = 0
    y = 0
    while y < len(grid[x]):
        while x < len(grid):
            print(grid[x][y], end="")
            x += 1
        print("\n")
        y += 1
        x = 0

picGrid(grid)
