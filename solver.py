from queue import PriorityQueue
import math
import numpy as np

class PuzzleSolver:
    def __init__(self, board):
        self.board = board
        self.size = 0

    def make_move(self, zero_pos, direction, board):
        x, y = zero_pos
        if direction == "up" and x > 0:
            board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
            return True
        elif direction == "down" and x < self.size - 1:
            board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
            return True
        elif direction == "left" and y > 0:
            board[x][y], board[x][y-1] = board[x][y-1], board[x][y]
            return True
        elif direction == "right" and y < self.size - 1:
            board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
            return True
        return False

    def get_zero_position(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    return (i, j)

    def manhattan_distance(self, board):
        distance = 0
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] != 0:
                    x, y = divmod(board[i][j]-1, self.size)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def is_solvable(self):
        board_flat = [item for sublist in self.board for item in sublist]
        inversions = 0
        for i in range(self.size):
            for j in range(i+1, self.size):
                if board_flat[i] != 0 and board_flat[j] != 0 and board_flat[i] > board_flat[j]:
                    inversions += 1
        return inversions % 2 == 0

    def solve(self):
        start_board = tuple(item for sublist in self.board for item in sublist)
        goal_board = tuple(list(range(1, self.size*self.size)) + [0])
        queue = PriorityQueue()
        queue.put((0, 0, start_board, []))  # The fourth parameter is a list to store the sequence of steps
        visited = {start_board}

        while not queue.empty():
            priority, moves, current_board, path = queue.get()

            if current_board == goal_board:
                return moves, path

            current_board_2d = [list(current_board[i*self.size:(i+1)*self.size]) for i in range(self.size)]
            zero_pos = self.get_zero_position(current_board_2d)

            for direction in ["up", "down", "left", "right"]:
                new_board = [row.copy() for row in current_board_2d]
                if self.make_move(zero_pos, direction, new_board):
                    new_zero_pos = self.get_zero_position(new_board)
                    new_board_flat = tuple(item for sublist in new_board for item in sublist)
                    if new_board_flat not in visited:
                        visited.add(new_board_flat)
                        queue.put((moves + 1 + self.manhattan_distance(new_board), moves + 1, new_board_flat, path + [direction]))

        return -1, []


    def check_ele(self,ele):
        return ele.isdigit()

    def check_valid_board(self):

        # Check if it is a square number
        if math.ceil(math.sqrt(self.size)) != math.floor(math.sqrt(self.size)):
            raise Exception("Not valid input: Number of elements of input is not a perfect square.")

        # Check if duplicates are in the board or non-consecutive numbers in the board.
        print(self.size)
        print(type(self.size))

        if set(self.board) != set(range(self.size)):
            raise Exception("Not valid input: All the number must start from 0 to number of squares - 1, each number needs to be unique.")

        return True

    def create_board(self):

        while True:

            ele = input()
            if ele.lower() == "stop":
                break

            if not self.check_ele(ele):
                print("Invalid input, please try again.")   
            else: 
                self.board.append(int(ele))
        print(self.board)
        self.size = len(self.board)
        if self.check_valid_board():        
            self.size = int(math.sqrt(self.size))
            self.board = list(np.array(self.board).reshape((self.size,self.size)))
            print("Board successfully entered.")
        
            
def main():
    print("Input the matrix one by one with row order. The empty square is represented as 0. End your input with 'stop'. ")
    solver = PuzzleSolver([])

    solver.create_board()

    if solver.is_solvable():
        moves, steps = solver.solve()
        print("Minimum number of moves:", moves)
        for i, step in enumerate(steps, 1):
            print(f"Step {i}: Move the empty tile {step}")
    else:
        print("This puzzle is not solvable.")

if __name__ == "__main__":

    main()