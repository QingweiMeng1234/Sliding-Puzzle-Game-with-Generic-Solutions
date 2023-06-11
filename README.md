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

### Filtering out unsolvable puzzles
The puzzle is solvable if and only if it has an even permutation. If we consider each board position as a permutation, any valid move does not change the permutation. Since the final position is an even permutation, only puzzles with an even permutation is solvable. 

## Solver Algorithm Explanation
I have applied a Heuristic Search Algorithm. It works by exploring possible moves, favoring those that seem to lead towards a solution. For this algorithm, the heuristic is the Manhattan distance from each tile to its goal position.

Below are the details of the algorithm:

### 1. Initiate a priority queue with the following entries:

- The sum of the number of moves made so far and the estimated moves remaining (measured by the Manhattan Distance).
- The number of moves that have already been made.
- The current board configuration.
- The path that has been taken so far.

### 2. While the queue is not empty:

#### 2.1 Remove the top element from the queue.

- If the current board configuration matches our target configuration:
  - Terminate the loop.

#### 2.2 Get the position of the blank tile on the board.

#### 2.3 For each possible direction:

- Move the blank tile in the current direction to create a new board configuration.
- If this new board configuration has not been encountered before:
  - Record this new configuration in the "visited" list.
  - Add a new entry to the queue, with the following elements:
    - The sum of the number of moves made so far and the estimated remaining moves, incremented by 1.
    - The total number of moves made, incremented by 1.
    - The new board configuration.
    - The path taken so far, appended with the new direction.

### 3. Output:

- Return the path taken and the total number of steps taken.


This algorithm mimics the Dijkstra's algorithm, an algorithm for finding the shortest paths between nodes in a weighted graph. In this scenario, the path consists of the moves the user makes. Each node is a board position. Each edge is a possible direction to move at a specific board position. 

## Complexity Analysis:
It is not easy to analyze this algorithm's complextiy. It is bounded by the Dijkstra's Algorithm with $O((\sqrt{n}!)^2) = O(n^n)$. However, since there is only a small fraction of board being explored. the average case is going to be much better.

## Memory Analysis:
The memory is bounded by O(n^n). However, the average usage would be much better since we are not using all the possible board positions.

