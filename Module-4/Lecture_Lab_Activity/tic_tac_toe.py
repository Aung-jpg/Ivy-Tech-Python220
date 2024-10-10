board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
locations = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]

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
            if board[i][j] == 0:
                free_fields.append((i, j))
    return free_fields

def enter_move(board):
    locations = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]
    free_fields = make_list_of_free_fields(board)
    numbers = [locations[i[0]][i[1]] for i in free_fields]

    display_board(locations)
    print("You can only go in the following spaces")
    print(numbers)
    space = int(input("where do you wanna go: "))
    
    for i in range(len(locations)):
        for j in range(len(locations[i])):
            if locations[i][j] == space:
                board[i][j] = "O"



display_board(locations)
print("locations you can place your 'O'")

display_board(board)

# computer's move
board[1][1] = "X"

display_board(board)

print("your turn, remember you can't go into a place that's already taken")
print(make_list_of_free_fields(board))
enter_move(board)
display_board(board)
