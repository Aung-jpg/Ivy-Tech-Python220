board = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
locations = [[1, 2, 3], [4, 5, 6], [7, 8 ,9]]

def display_board(board):
    for i in range(len(board)):
        print()
        for j in board[i]:
            print(j, end="")
    else:
        print()

display_board(locations)
print("locations you can place your 'O'")

display_board(board)

# computer's move
board[1][1] = "X"

display_board(board)

