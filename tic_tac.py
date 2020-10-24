def print_board(matrix):
    board =""
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            if j < len(matrix[i]) - 1:
                text = " {element} |"
                board += text.format(element = str(matrix[i][j]))
            else:
                text = " {element} \n"
                board += text.format(element = str(matrix[i][j]))
        if i < len(matrix) - 1:
            board += ("---+---+---\n")
    print(board)



test_matrix = []
row = []
for x in range(0,3):
    row =[x,x,x]
    test_matrix.append(row)

print_board(test_matrix)
