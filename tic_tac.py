"""A tic tac toe game written in python"""
PLAYER = -1
CPU = 1
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

#Functions

def print_board(matrix):
    """ Prints the current state of the board"""
    game_board = ""
    for i, row in enumerate(matrix):
        if i == 0:
            game_board += " A   B   C \n \n"
        for j, cell in enumerate(row):
            placeholder = get_placeholder(cell)
            if j < len(row) - 1:
                text = " {element} |"
                game_board += text.format(element = placeholder)
            else:
                text = " {element}   {row_number}\n"
                game_board += text.format(element = placeholder, row_number = i)
        if i < len(matrix) - 1:
            game_board += ("---+---+---\n")
    print(game_board)

def get_placeholder(cell):
    """Returns appropriate placeholder based on the cell value"""
    if cell == -1:
        placeholder = "X"
    elif  cell == 1:
        placeholder = "O"
    else:
        placeholder = " "
    return placeholder

def get_winner(matrix):
    """ Checks the state of the board to see i a player has won"""
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

def get_move():
    """Gets human player input"""
    print("Insert column letter")
    column = input()
    while not validate_columns(column):
        print("Invalid input, insert column letter")
        column = input()
    if column == "a":
        column_index = 0
    elif column == "b":
        column_index = 1
    elif column == "c":
        column_index = 2
    print("Insert row number")
    row_index = input()
    while not validate_rows(row_index):
        print("Invalid input, insert row number")
        row_index = input()
    return (int(row_index), column_index)

def validate_columns(column_id):
    """Validates columns input"""
    validated = False
    if not isinstance(column_id,str):
        validated = False
    elif column_id.lower() == "a" or column_id.lower() =="b" or column_id.lower() =="c":
        validated = True
    else:
        validated = False
    return validated

def validate_rows(row_id):
    """Validate rows input"""
    validated = False
    if not row_id.isdigit():
        validated = False
    elif int(row_id) == 0 or int(row_id) == 1 or int(row_id) == 2:
        validated = True
    else:
        validated= False
    return validated

def set_board_cell(x_move, y_move, player):
    """Sets the selected cell for the player or the cpu"""
    board[x_move][y_move] = player

while get_winner(board) != -1:
    #player turn
    print_board(board)
    move = get_move()
    set_board_cell(move[0],move[1], PLAYER)
    #cpu turn
