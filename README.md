# Sliding-Puzzle-Game-with-Generic-Solutions

## Game Introduction
This game consists of a nxn grid with nxn - 1 numbered tiles and one blank space, which the player can slide into the empty space. The goal of the puzzle is to arrange the tiles into numerical order.

## Code Usage

This repo consists of two python files, puzzle.py and solver.py. Puzzle.py is the game. By running 
```
python puzzle.py
```

, it will ask the user for the size of the grid. Then the user tries to solve the puzzle by moving the empty tile to ensure all the tiles are in the numerical order. Solver.py is the solver. By running
```
python solver.py
```

It asks the user to put the number one by one in a row order, and then output the steps.

## Solver Algorithm Explanation
I have applied a Heuristic Search Algorithm. It works by exploring possible moves, favoring those that seem to lead towards a solution. For this algorithm, the heuristic is the Manhattan distance from each tile to its goal position.

Below are the details of the 

1. Initiate a priority queue with the following entries:
  - Number of moves has made so far and the estimated moves remaining (measured by the Mahattan Distance)
  - Number of moves that has already made,
  - The board at this position
  - The path that has already been taken.
