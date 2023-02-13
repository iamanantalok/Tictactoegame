import random
# displaying board

def display_board(board):
    print("   |   |   ")
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')
    print("   |   |   ")
    print('-----------')
    print("   |   |   ")
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6] + ' ')
    print("   |   |   ")
    print('-----------')
    print("   |   |   ")
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')
    print("   |   |   ")


# taking player input


def player_input():

    marker = ''

    while not(marker == 'X' or marker == 'O'):
        marker = input("Player 1:Do you want X or O").upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board

def place_marker(board,marker,position):
    board[position]=marker

# takes in a board and checks to see if someone has won


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
# the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.


def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# returns a boolean indicating whether a space on the board is freely available.

def space_check(board,position):
    return board[position] == ' '

# checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
    # Board is full if return true
    return True

# asks for a player's next position (as a number 1-9) and
#  then uses the function from step 6 to check if its a free position.
# If it is, then return the position for later use.

def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position

 # ask the player if they want to play again and returns a boolean True if they do want to play again.


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Use while loops and the functions you've made to run the game!

#while loop too keep running the game

print("Welcom to Tic Tac Toe")

while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to Play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Congratulation!You have won the game')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break

                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break













