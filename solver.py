from queue import PriorityQueue

def make_move(board, zero_pos, direction):
    x, y = zero_pos
    if direction == "up" and x > 0:
        board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
        return True
    elif direction == "down" and x < len(board) - 1:
        board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
        return True
    elif direction == "left" and y > 0:
        board[x][y], board[x][y-1] = board[x][y-1], board[x][y]
        return True
    elif direction == "right" and y < len(board) - 1:
        board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
        return True
    return False


def get_zero_position(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)

def get_possible_moves(board):
    zero_pos = get_zero_position(board)
    possible_moves = []
    if zero_pos[0] > 0:
        possible_moves.append((zero_pos[0] - 1, zero_pos[1]))
    if zero_pos[0] < len(board) - 1:
        possible_moves.append((zero_pos[0] + 1, zero_pos[1]))
    if zero_pos[1] > 0:
        possible_moves.append((zero_pos[0], zero_pos[1] - 1))
    if zero_pos[1] < len(board[0]) - 1:
        possible_moves.append((zero_pos[0], zero_pos[1] + 1))
    return possible_moves

def manhattan_distance(board):
    size = len(board)  # Assume the board is a square
    distance = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                x, y = divmod(board[i][j]-1, size)
                distance += abs(x - i) + abs(y - j)
    return distance


def solve(board):

    size = len(board) 
    start_board = tuple(item for sublist in board for item in sublist)
    goal_board = tuple(list(range(1, size*size)) + [0])
    
    # Priority queue
    queue = PriorityQueue()
    queue.put((0, 0, start_board, []))  # The fourth parameter is a list to store the sequence of steps
    
    # Visited boards
    visited = {start_board}
    
    while not queue.empty():
        priority, moves, current_board, path = queue.get()
        # print("Current board:", current_board)  # Print the current board
        # print("Current path:", path)  # Print the current sequence of moves

        if current_board == goal_board:
            return moves, path
            
        current_board_2d = [list(current_board[i*size:(i+1)*size]) for i in range(size)]
        zero_pos = get_zero_position(current_board_2d)
        
        for direction in ["up", "down", "left", "right"]:
            new_board = [row.copy() for row in current_board_2d]
            if make_move(new_board, zero_pos, direction):
                new_zero_pos = get_zero_position(new_board)
                new_board_flat = tuple(item for sublist in new_board for item in sublist)
                if new_board_flat not in visited:
                    visited.add(new_board_flat)
                    queue.put((moves + 1 + manhattan_distance(new_board), moves + 1, new_board_flat, path + [direction]))

    return -1, []
def is_solvable(board):
    """Check if a puzzle is solvable.
    
    According to the theorem about parity in permutations,
    a puzzle is solvable if and only if the number of inversions
    is even.
    
    An inversion is when a tile precedes another tile with a lower
    number on it.
    """
    size = len(board)
    board_flat = [item for sublist in board for item in sublist]
    inversions = 0
    for i in range(size*size):
        for j in range(i+1, size*size):
            # Don't count the blank
            if board_flat[i] != 0 and board_flat[j] != 0 and board_flat[i] > board_flat[j]:
                inversions += 1
    print(inversions)
    return inversions % 2 == 0

# Example usage
board = [[1,5,3],[2,4,0],[8,6,7]]

if is_solvable(board):
    moves, steps = solve(board)
    print("Minimum number of moves:", moves)
    for i, step in enumerate(steps, 1):
        print(f"Step {i}: Move the empty tile {step}")
else:
    print("This puzzle is not solvable.")

