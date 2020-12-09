"""
Tic Tac Toe Player
"""

import math
import copy

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
    x = 0
    o = 0

    for i in range(3):
        for j in range(3):
            if(board[i][j] == X):
                x += 1
            elif(board[i][j] == O):
                o += 1

    if(x > o):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # print("ehyy")
    if(board[action[0]][action[1]] == EMPTY):
        board_copy = copy.deepcopy(board)
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    else:
        raise NameError("Invalid Move - That cell is already occupied")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if((board[0][0] == X) and (board[1][0] == X) and (board[2][0] == X)):
        return X
    elif((board[0][1] == X) and (board[1][1] == X) and (board[2][1] == X)):
        return X
    elif((board[0][2] == X) and (board[1][2] == X) and (board[2][2] == X)):
        return X
    elif((board[0][0] == X) and (board[0][1] == X) and (board[0][2] == X)):
        return X
    elif((board[1][0] == X) and (board[1][1] == X) and (board[1][2] == X)):
        return X
    elif((board[2][0] == X) and (board[2][1] == X) and (board[2][2] == X)):
        return X
    elif((board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X)):
        return X
    elif((board[0][2] == X) and (board[1][1] == X) and (board[2][0] == X)):
        return X
    elif((board[0][0] == O) and (board[1][0] == O) and (board[2][0] == O)):
        return O
    elif((board[0][1] == O) and (board[1][1] == O) and (board[2][1] == O)):
        return O
    elif((board[0][2] == O) and (board[1][2] == O) and (board[2][2] == O)):
        return O
    elif((board[0][0] == O) and (board[0][1] == O) and (board[0][2] == O)):
        return O
    elif((board[1][0] == O) and (board[1][1] == O) and (board[1][2] == O)):
        return O
    elif((board[2][0] == O) and (board[2][1] == O) and (board[2][2] == O)):
        return O
    elif((board[0][0] == O) and (board[1][1] == O) and (board[2][2] == O)):
        return O
    elif((board[0][2] == O) and (board[1][1] == O) and (board[2][0] == O)):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != None):
        return True
    try:
        actions(board).pop()
        return False
    except KeyError:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    elif(winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_turn = player(board)

    if player_turn == X:
        best = 1
        neutral = 0
        worst = -1
    elif player_turn == O:
        best = -1
        neutral = 0
        worst = 1

    if terminal(board):
        return None

    possible_moves = list(actions(board))
    possible_moves_utilites = []

    for move in possible_moves:
        temp = custom_function(result(board, move))
        possible_moves_utilites.append(temp)

        if temp == best:
            break

    try:
        return possible_moves[possible_moves_utilites.index(best)]
    except ValueError:

        try:
            return possible_moves[possible_moves_utilites.index(neutral)]
        except ValueError:

            try:
                return possible_moves[possible_moves_utilites.index(worst)]
            except ValueError:
                pass


def custom_function(board):

    player_turn = player(board)

    if player_turn == X:
        best = 1
        neutral = 0
        worst = -1
    elif player_turn == O:
        best = -1
        neutral = 0
        worst = 1

    if terminal(board) == True:
        return utility(board)

    possible_actions = list(actions(board))
    move_utilities = []

    for items in possible_actions:
        temp = custom_function(result(board, items))
        move_utilities.append(temp)

        if temp == best:
            break

    try:
        return move_utilities[move_utilities.index(best)]
    except ValueError:

        try:
            return move_utilities[move_utilities.index(neutral)]
        except ValueError:

            try:
                return move_utilities[move_utilities.index(worst)]
            except ValueError:
                pass
