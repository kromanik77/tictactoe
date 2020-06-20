# Tic-Tac-Toe Evaluation
#
# This program evaluates an N X N tic-tac-toe board to see if there is
# a winner. If so, it prints whether it found a row, column or diagonal
# match and it prints the winning value.
#
# Notes:
# 1. It assumes the tic-tac-toe board is given as a list of lists, where
#    the first element of the top level list is the first row of the board.
# 2. It doesn't read input. The top level function is called "check", which
#    takes a board as input.
# 3. It makes sure the given board is N X N and exits with an error if not.
# 4. It makes no assumptions about how many different values are on the
#    board or if they are strings or numbers (easy to do in Python).

# Check whether board is N X N
def is_valid(board):
    valid=True
    rows=len(board)
    for row in board:
        cols=len(row)
        if cols != rows:
            valid=False
    return valid

# Evaluate a tic-tac-toe board to see if there's a winner.
# Checks for a row match first, then a column match, then diagonals.
# Note that it returns when it finds the first match, so if there
# are multiple matches, only the first one is found and returned.
# Returns the winning value, or None if there is no winner.
def evaluate(board):
    winner=None # Return the winning value if any
    size=len(board) # Size is N if board is N X N
    
    # Check for a row with all the same values
    for row in board:
        first=row[0]
        match=True
        for elem in row:
            if elem != first:
                match=False
        if match:
            print("Row match")
            winner=first
            return winner
    
    # Check for a column with all the same chars
    row1=board[0]
    for i in range(size):
        first=row1[i]
        match=True
        for row in board:
            if row[i] != first:
                match=False
        if match:
            print("Column match")
            winner=first
            return winner

    # Check forward diagonal
    first=board[0][0]
    match=True
    for i in range(size):
        if board[i][i] != first:
            match=False
    if match:
        print("Forward diagonal match")
        winner=first
        return winner

    # Check backward diagonal
    first=board[0][size-1]
    match=True
    for i in range(size):
        if board[i][size-1-i] != first:
            match=False
    if match:
        print("Backward diagonal match")
        winner=first
        return winner

    return winner

# Checks whether the board is valid and if so, evaluates it to see
# if there is a winner.
def check(board):
    print("board = ", board)
    if is_valid(board):
        winner=evaluate(board)
        if winner != None:
            print("The winner is ", winner)
        else:
            print("There is no winner")
    else:
        print("Board is invalid - it must be an N X N board")

board1=(('X','X','O'),('X','O','O'),('X','O','X'))
check(board1)

board2=(('X','X','O'),('O','O','O'),('X','O','X'))
check(board2)

board3=(('X','X','O'),('X','X','O'),('O','O','X'))
check(board3)

board4=(('X','X','O'),(1,'X',1),(2,3,'X'))
check(board4)

board5=(('X','O','O'),('O','X','X'),('X','X','O'))
check(board5)

board6=((1,1,1,1),(2,2,2,2),(3,3,3,3),(4,4,4,4))
check(board6)

board7=((4,2,1,1),(2,4,3,2),(3,3,4,3),(4,1,4,4))
check(board7)

board8=((1,2,1,1),(2,4,1,2),(3,1,4,3),(1,1,4,4))
check(board8)

board9=((1,1,1,1),(2,2,2),(3,3,3,3),(4,4,4,4))
check(board9)

board10=((4,2,1,1),(2,4,3,2),(3,3,4,3))
check(board10)
