**GAME OF LIFE SIMULATION WITH PYGAME--**

This document details the instructions for running the included Python code, which simulates John Conway's Game of Life using the Pygame library.

***PREREQUISITES:***
Python 3.x (not included)
Pygame library (installation instructions: https://www.pygame.org/wiki/GettingStarted)

***EXECUTING THE FILE:***
Download the main.py file and run it using the terminal
Grid Size:
The script will prompt you to enter the desired width and height of the simulation grid. 
*SUGGESTED HEIGHT AND WIDTH = 35 x 35*

***USER INTERACTION:***
*Mouse Click:*
1. Clicking on a cell will toggle its state between alive (green) and dead (soil color).

*Keyboard Controls:*
1. Spacebar: Pauses and unpauses the simulation.
***if the grid is blank, just press the spacebar and the simulation will be alive: a pattern will get loaded and start running atonce***
2. Delete: Clears all living cells from the grid.
3. R: Generates a random pattern of living cells.
***if you want to witness the real fun of this simulation, just press r and then spacebar (to play)***
4. Tab: Advances the simulation by one generation (useful for slower observation).
5. Numbers 1-0: Load pre-defined patterns ("glider," "blinker," etc.) for exploration.

***DESCRIPTION:***
This program utilizes Pygame to visualize the cellular automata known as Conway's Game of Life. The simulation starts with a user-defined grid of cells, each being either alive or dead. The evolution of the system follows these rules:

1. Any live cell with fewer than two live neighbors dies in the next generation (underpopulation).
2. Any live cell with two or three live neighbors remains alive in the next generation (survival).
3. Any live cell with more than three live neighbors dies in the next generation (overcrowding).
4. Any dead cell with exactly three live neighbors becomes a live cell in the next generation (birth).

The simulation continuously updates the grid based on these rules, allowing for emergent patterns and complex behavior.