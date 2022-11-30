#!/usr/bin/python3
"""island_perimeter module"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if we find a land cell, add 4 to the perimeter
            if grid[i][j] == 1:
                perimeter += 4
                # check if the cell is connected to the NESW neighbors
                # if it is, subtract 2 from the perimeter

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
