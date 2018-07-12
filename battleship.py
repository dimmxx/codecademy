from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print "  ".join(row)


print_board(board)
print "-------------"


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

a = ship_row
b = ship_col1

board[a][b] = "W"

print_board(board)

print ship_row
print ship_col

print a
print b

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Write your code below!
if ship_row == guess_row and ship_col == guess_col:
    print ("Congratulations! You sank my battleship!")
else:
    print "You missed my battleship!"
    board[guess_row - 1][guess_col - 1] = "X"
    print_board(board)