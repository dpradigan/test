import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
   # The initial state of the board is a list of 3 lists each containing 3 elements.  This list of lists represents the tic tac toe board.  The initial state of each element is empty representing a blank tic tac toe board.
   
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # X always starts the game, therefore O will only have a turn when X is already on the board.  Implement a count of both X, and O on the board and iterate through the entire board (list of lists).  If X is greater than O, O is up.  Else it is X's turn unless the game has ended.
    
    XCount = 0
    OCount = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                XCount += 1
            elif board [i][j] == O:
                OCount += 1
    if XCount > OCount:
        return O
    else:
        return X
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # This returns a set of all possible remaining actions.  It iterates through the entire board and returns a set of the currently empty squares.
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append([i, j])
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Without try errors kept occuring.  This creates a copy of the current player board then adds the result of move (i,j) and returns the new board.
    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardcopy[action[0]][action[1]] = player(boardcopy)
            return boardcopy
    except IndexError:
        print("Index Error")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
     # Check rows for a winner
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # Check columns for a winner
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # Check diagonals for a winner
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks to see if winner has returned a winner.  If it has then the game is terminal.  Also checks to see that there are no empty squares within the board, and the winner is none.  Essentially checking if all moves have been made.  If either is true, true is returned and the game is terminal.

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
        
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Above description is self explanatory.
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
#This was developed using following website https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
    current_player = player(board)

    if current_player == X:
        best = -math.inf
        for action in actions(board):
            temp = min_value(result(board, action))
            if temp > best:
                best = temp
                best_move = action
    else:
        best = math.inf
        for action in actions(board):
            temp = max_value(result(board, action))
            if temp < best:
                best = temp
                best_move = action
    return best_move

def max_value(board):
#This was developed using following website https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
    if terminal(board):
        return utility(board)
    best = -math.inf
    for action in actions(board):
        best = max(best, min_value(result(board, action)))
    return best

def min_value(board):
#This was developed using following website: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
    if terminal(board):
        return utility(board)
    best = math.inf
    for action in actions(board):
        best = min(best, max_value(result(board, action)))
    return best
