"""
Tic Tac Toe Player
"""

import math
import copy
# from util import Node, StackFrontier, QueueFrontier

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    circles = sum(map(lambda row: row.count(O), board))
    crosses = sum(map(lambda row: row.count(X), board))
    if circles >= crosses:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                moves.append((row, col))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #TODO: Revisar
    row, col = action
    board_tmp = copy.deepcopy(board)
    board_tmp[row][col] = player(board)
    return board_tmp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
     
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]  # Horizontal win -
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]  # Vertical win |
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]  # Diagonal win \
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]  # Diagonal win /
    return None  # No winner

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or len(actions(board)) == 0:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
     Returns the optimal action for the current player on the board.
     """
    if terminal(board):
        return None

    if player(board) == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            child_board = result(board, action)
            score = minimax_score(child_board)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    else: # el siguiente es el O
        best_score = math.inf
        best_action = None
        for action in actions(board):
            child_board = result(board, action)
            score = minimax_score(child_board)
            if score < best_score:
                best_score = score
                best_action = action
        return best_action

def minimax_score(board):
    if terminal(board):
        return utility(board)

    if player(board) == X:
        best_score = -math.inf
        for action in actions(board):
            child_board = result(board, action)
            score = minimax_score(child_board)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for action in actions(board):
            child_board = result(board, action)
            score = minimax_score(child_board)
            best_score = min(best_score, score)
        return best_score