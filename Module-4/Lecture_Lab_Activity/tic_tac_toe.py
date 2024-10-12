from random import choice

def display_board(board):
    for i in range(len(board)):
        print()
        for j in board[i]:
            print(j, end="")
    else:
        print()

def make_list_of_free_fields(board):
    free_fields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "X" and board[i][j] != "O":
                free_fields.append((i, j))
    return free_fields

def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    numbers = [board[i[0]][i[1]] for i in free_fields]

    print("You can only go in the following spaces")
    print(numbers)

    active = True
    while active:
        try:
            space = int(input("where do you wanna go: "))
        except ValueError:
            continue
        if space in numbers:
            active = False
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == space:
                board[i][j] = "O"

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    numbers = [board[i[0]][i[1]] for i in free_fields]
    move = choice(numbers)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move:
                board[i][j] = "X"

def victory_for(board, sign):   
    locations = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == sign:
                locations.append((i, j))

    # vertical victory
    if (0, 0) in locations and (1, 0) in locations and (2, 0) in locations:
        return True
    if (0, 1) in locations and (1, 1) in locations and (2, 1) in locations:
        return True
    if (0, 2) in locations and (1, 2) in locations and (2, 2) in locations:
        return True
    
    # horizontal vic royale
    if (0, 0) in locations and (0, 1) in locations and (0, 2) in locations:
        return True
    if (1, 0) in locations and (1, 1) in locations and (1, 2) in locations:
        return True
    if (2, 0) in locations and (2, 1) in locations and (2, 2) in locations:
        return True
    
    # this "\" diagonal victory
    if (0, 0) in locations and (1, 1) in locations and (2, 2) in locations:
        return True
    # this "/" diagonal victory
    if (0, 2) in locations and (1, 1) in locations and (2, 0) in locations:
        return True
    # if nothing
    return False
    

board = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

display_board(board)
# computer's move
board[1][1] = "X"
display_board(board)

player_win_status = victory_for(board, "O")
computer_win_status = victory_for(board, "X")
free_fields = make_list_of_free_fields(board)

while player_win_status is False and computer_win_status is False and free_fields != []:
    enter_move(board)
    display_board(board)
    player_win_status = victory_for(board, "O")
    computer_win_status = victory_for(board, "X")
    if player_win_status or computer_win_status:
        break
    draw_move(board)
    display_board(board)
    free_fields = make_list_of_free_fields(board)
    player_win_status = victory_for(board, "O")
    computer_win_status = victory_for(board, "X")

if player_win_status:
    print("The Player Won")

if computer_win_status:
    print("The Computer Won")

if not player_win_status and not computer_win_status:
    print("Tie")
