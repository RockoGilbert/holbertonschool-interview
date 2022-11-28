#!/usr/bin/python3
'''
function def island_perimeter(grid):
that returns the perimeter of the island described in grid:
grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesnt have “lakes”
        (water inside that isnt connected to the
            water surrounding the island).
'''


def island_perimeter(grid):

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if we find a land cell, add 4 to the perimeter.
            if grid[i][j] == 1:
                perimeter += 4
                # then, check if the cell is connected to the NESW neighbors
                # if it is, subtract 2 from the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
<<<<<<< HEAD
    
=======
>>>>>>> 901672072be6f556af12656c4fc1160542d764cb
