board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]


current_player = "X"

end = False

winner = None

turn = 0


def display_board():
    print("\n")
    print("{} | {} | {}\n- - - - -\n{} | {} | {}\n- - - - -\n{} | {} | {}".format(*board))


def handle_turn():
    #handle a single turn
    global turn
    global end

    valid = False
    print(current_player + "'s turn")
    position = input("Input the index number of the board: ")
    
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            display_board()
            print("It is not a valid move! Try again.")
            position = input("Choose a position from 1-9: ")
        
        square = position
        position = int(position) - 1

        if type(board[position]) is int:
            board[position] = current_player
            valid = True
    
    turn = turn + 1
    
    display_board()
    print(current_player + " makes a move to square " + square + ".")




#for each element in row check if they equal to row[0]
#eg: board[0:3] ["X", "X", "X"]
#row[0] = board[0] = x
#1_iter: x = board[0] = x = row[0] <-return true
#2_iter: x = board[1] = x = row[0] <-return true
#3_iter: x = board[2] = x = row[0] <-return true
#return true only True and True and True
def check_same(row):
    return all(x == row[0] for x in row)


def check_if_win():
    return check_same(board[0:3]) or check_same(board[3:6]) or check_same(board[3:6]) or check_same(board[6:9]) or check_same(board[::3]) or check_same(board[1::3]) or check_same(board[2::3]) or check_same(board[::4]) or check_same(board[2:7:2])


def flip_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"


def play():
    global end
    global winner
    global current_player
    display_board()

    while not end:
        handle_turn()

        if check_if_win():
            end = True
            winner = current_player
        
        if turn == 9:
            end = True


        flip_player()

    
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("It's a tie.")




play()
