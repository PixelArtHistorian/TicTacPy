"""
A tic tac toe game written in python
"""
import random
import platform
import time
import math
import os

PLAYER = -1
CPU = 1
INFINITY = math.inf
PLAYERTOKEN = ""
CPUTOKEN = ""
EXIT = False
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

#Functions

def print_board(matrix, p_token, cpu_token):
    """
    Prints the current state of the board
    """
    game_board = ""
    for i, row in enumerate(matrix):
        if i == 0:
            game_board += " A   B   C \n \n"
        for j, cell in enumerate(row):
            placeholder = get_placeholder(cell, p_token, cpu_token)
            if j < len(row) - 1:
                text = " {element} |"
                game_board += text.format(element = placeholder)
            else:
                text = " {element}   {row_number}\n"
                game_board += text.format(element = placeholder, row_number = i)
        if i < len(matrix) - 1:
            game_board += ("---+---+---\n")
    print(game_board)

def get_placeholder(cell, p_token, cpu_token):
    """
    Returns appropriate placeholder based on the cell value
    """
    if cell == -1:
        placeholder = p_token
    elif  cell == 1:
        placeholder = cpu_token
    else:
        placeholder = " "
    return placeholder

def clean():
    """
    Cleans the console
    """
    os_name = platform.system().lower()
    if "windows" in os_name:
        os.system('cls')
    else:
        os.system('clear')

def get_winner(matrix):
    """
    Checks the state of the board to see i a player has won
    """
    #check first diagonal
    diagonal1 = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if i == j:
                diagonal1.append(cell)
    if len(set(diagonal1)) == 1:
        return diagonal1[0]
    #check second diagonal
    diagonal2 = []
    for i in reversed(range(0, len(matrix))):
        for j in reversed(range(0, len(matrix[i]))):
            if i == j:
                diagonal2.append(matrix[i][j])
    if len(set(diagonal1)) == 1:
        return diagonal1[0]
    #check rows
    for i, row in enumerate(matrix):
        if len(set(row)) == 1:
            return row[0]
    #check columns
    column = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            column.append(cell)
        if len(set(column)) == 1:
            return cell
    return 0

def minimax(board_state, depth, player):
    """
    Function that finds the optimal move for the specified player
    """
    if player == CPU:
        best = [-1, -1, -INFINITY]
    else:
        best =[-1, -1, INFINITY]

    if depth == 0 or get_winner(board) != 0:
        score = get_winner(board_state)
        return[-1,-1, score]

    for cell in get_free_cells(board_state):
        x_index ,y_index  = cell[0], cell[1]
        board_state = change_board_state(x_index, y_index, player, board_state)
        score = minimax(board_state, depth - 1, -player)
        board_state = change_board_state(x_index, y_index, 0, board_state)
        score[0], score[1] = x_index, y_index

        if player == CPU:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score
    return best

def get_move():
    """
    Gets human player input
    """
    print("Insert column letter")
    column = input().strip()
    while not validate_columns(column):
        print("Invalid input, insert column letter")
        column = input().strip()
    if column == "a":
        column_index = 0
    elif column == "b":
        column_index = 1
    elif column == "c":
        column_index = 2
    print("Insert row number")
    row_index = input().strip()
    while not validate_rows(row_index):
        print("Invalid input, insert row number")
        row_index = input().strip()
    return (int(row_index), column_index)

def cpu_move(board_state):
    """
    Functions that uses the minimax function to find the optimal move for the cpu
    """
    depth = len(get_free_cells(board_state))
    if depth == 0 or get_winner(board) != 0:
        return
    if depth == 9:
        return random.choice(get_free_cells(board))
    else:
        move = minimax(board_state, depth, CPU)
        return move

def validate_columns(column_id):
    """
    Validates columns input
    """
    validated = False
    if not isinstance(column_id,str):
        validated = False
    elif column_id.lower() == "a" or column_id.lower() =="b" or column_id.lower() =="c":
        validated = True
    else:
        validated = False
    return validated

def validate_rows(row_id):
    """
    Validate rows input
    """
    validated = False
    if not row_id.isdigit():
        validated = False
    elif int(row_id) == 0 or int(row_id) == 1 or int(row_id) == 2:
        validated = True
    else:
        validated= False
    return validated

def validate_token_choice(choice):
    """
    Validates player token choice
    """
    return choice.isalpha() and (choice.upper() == "X" or choice.upper() == "O")

def validate_exit(choice):
    """
    Validates player choice to exit or continue playing
    """
    return choice.isalpha() and (choice.upper() == "Play" or choice.upper() == "Exit")

def change_board_state(x_move, y_move, player, board_state):
    """
    Sets the selected cell for the player or the cpu
    """
    board_state[x_move][y_move] = player
    return board_state

def get_free_cells(matrix):
    """
    Gets free cells list
    """
    free_cells = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 0:
                free_cells.append((i,j))
    return free_cells

#Main loop
print("Type X or O to chose your tokens, X always goes first")
player_choice = input().strip()
while not EXIT:

    while not validate_token_choice(player_choice):
        print("Invalid token, please select X or O")
        player_choice = input().strip()
    if player_choice.upper() == "X":
        PLAYERTOKEN = "X"
        CPUTOKEN = "O"
    else:
        PLAYERTOKEN = "O"
        CPUTOKEN = "X"

    while len(get_free_cells(board)) !=0 and get_winner(board) == 0:
        if PLAYERTOKEN.upper() == "X":
            #Player Turn
            print("Player turn (X)")
            print_board(board, PLAYERTOKEN, CPUTOKEN)
            move_player = get_move()
            board = change_board_state(move_player[0], move_player[1], PLAYER, board)
            clean()
            #cpu turn
            print("CPU turn (O)")
            move_CPU = cpu_move(board)
            board = change_board_state(move_CPU[0], move_CPU[1], CPU, board)
            time.sleep(2)
            clean()
        else:
            #cpu turn
            print("CPU turn (X)")
            move_CPU = cpu_move(board)
            board = change_board_state(move_CPU[0], move_CPU[1], CPU, board)
            time.sleep(2)
            clean()
            #Player Turn
            print("Player turn (O)")
            print_board(board, PLAYERTOKEN, CPUTOKEN)
            move_player = get_move()
            board = change_board_state(move_player[0], move_player[1], PLAYER, board)
            clean()

    if get_winner(board) == 1:
        print("CPU wins")
    elif get_winner(board) == 1:
        print("You win")
    else:
        print("It's a draw")
    time.sleep(1)
    print("Type 'Play' to play again or 'Quit' to exit")
    exit_choice = input().strip()
    while not validate_exit(exit_choice):
        print("Type 'Play' to play again or 'Quit' to exit")
    EXIT = exit_choice.upper() == "QUIT"

