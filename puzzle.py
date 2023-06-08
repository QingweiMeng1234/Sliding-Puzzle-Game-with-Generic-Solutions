import random

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.board = self.create_puzzle()
        
    def create_puzzle(self):
        while True:
            numbers = list(range(1, self.size * self.size)) + [""]
            random.shuffle(numbers)
            puzzle = [numbers[i:i+self.size] for i in range(0, self.size*self.size, self.size)]
            if self.is_solvable(puzzle):
                break
        return puzzle

    def is_solvable(self, board):
        board_flat = [item for sublist in board for item in sublist]
        inversions = 0
        for i in range(self.size*self.size):
            for j in range(i+1, self.size*self.size):
                if board_flat[i] != "" and board_flat[j] != "":
                    if board_flat[i] > board_flat[j]:
                        inversions += 1
        return inversions % 2 == 0

    def display_puzzle(self):
        line = "+---+---" * self.size + "+"
        for row in self.board:
            print(line)
            print("|", end="")
            for number in row:
                print(f" {number or ' '}\t|", end="")
            print()
        print(line)

    def get_blank_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == "":
                    return i, j

    def is_solved(self):
        number = 1
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] != number and (i != self.size-1 or j != self.size-1):
                    return False
                number += 1
        return True

    def move_up(self):
        i, j = self.get_blank_position()
        if i > 0:
            self.board[i][j], self.board[i-1][j] = self.board[i-1][j], self.board[i][j]

    def move_down(self):
        i, j = self.get_blank_position()
        if i < self.size - 1:
            self.board[i][j], self.board[i+1][j] = self.board[i+1][j], self.board[i][j]

    def move_left(self):
        i, j = self.get_blank_position()
        if j > 0:
            self.board[i][j], self.board[i][j-1] = self.board[i][j-1], self.board[i][j]

    def move_right(self):
        i, j = self.get_blank_position()
        if j < self.size - 1:
            self.board[i][j], self.board[i][j+1] = self.board[i][j+1], self.board[i][j]
            
    def play_game(self):
        
        while not self.is_solved():
            self.display_puzzle()
            move = input("Enter your move (w - up, s - down, a - left, d - right): ")
            if move == "w":
                self.move_up()
            elif move == "s":
                self.move_down()
            elif move == "a":
                self.move_left()
            elif move == "d":
                self.move_right()
            else:
                print("Invalid move! Please try again.")
                continue
        
        print("Congrtulations! You have solved the puzzle")
       
def main():
    size = int(input("Enter the size of the puzzle (e.g., 3 for a 3x3 puzzle): "))
    game = Puzzle(size)
    game.play_game()

# Call the main function
if __name__ == "__main__":
    main()