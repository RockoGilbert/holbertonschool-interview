#include "slide_line.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * slide_line - function that slides and merges an array of integers
 * @line: array of integers being slid
 * @size: number of elements
 * @direction: SLIDE_LEFT or SLIDE_RIGHT macro
 *
 * Return: 1 upon success, 0 upon failure
 */
int slide_line(int *line, size_t size, int direction)
{
	size_t idx, tmp;

	if (direction == SLIDE_LEFT)
	{
		slide_left(line, size);
		for (idx = 1; idx <= size && line[idx] != 0; idx++)
		{
			if (line[idx] == line[idx - 1])
			{
				line[idx - 1] *= 2;
				line[idx] = 0;
				tmp = 1;
			}
		}
		if (tmp)
		slide_left(line, size);
	}
	else if (direction == SLIDE_RIGHT)
	{
		slide_right(line, size);
		for (idx = size - 1; idx > 0 && line[idx - 1] != 0; idx--)
		{
			if (line[idx] == line[idx - 1])
			{
				line[idx] *= 2;
				line[idx - 1] = 0;
				tmp = 1;
			}
		}
		if (tmp)
			slide_right(line, size);
	}
	else
		return (0);

	return (1);
}

/**                                                                                                                             
 * slide_left - function that slides an array to the left                                                                       
 * @line: array of integers being slid                                                                                          
 * @size: number of elements                                                                                                    
 *                                                                                                                              
 * Return: void                                                                                                                 
 */
void slide_left(int *line, size_t size)
{
       size_t idx, y = 0;
       int tmp;
       
        for (idx = 0; idx < size && y < size; idx++)
        {
                while (line[y] != 0)
                        y++;

                if (line[idx] != 0 && idx > y)
                {
                        tmp = line[idx];
			line[idx] = line[y];
			line[y] = tmp;
                }
        }
}

/**                                                                                                                             
 * slide_right - function that slides an array to the right                                                                     
 * @line: array of integers being slid                                                                                          
 * @size: number of elements                                                                                                    
 *                                                                                                                              
 * Return: void                                                                                                                 
 */
void slide_right(int *line, size_t size)
{
        int idx, y = size - 1;
	int tmp;

        for (idx = size - 1; idx >= 0 && y >= 0; idx--)
        {
                while (line[y] != 0 && y > 0)
                        y--;

                if (line[idx] != 0 && idx < y)
                {
		        tmp = line[idx];
			line[idx] = line[y];
			line[y] = tmp;

                }
        }
}
