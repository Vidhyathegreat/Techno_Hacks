# Tic Tac Toe

# Display the game board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Check if a player has won
def check_win(board, mark):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[7] == mark and board[4] == mark and board[1] == mark) or
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        (board[9] == mark and board[6] == mark and board[3] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) or
        (board[9] == mark and board[5] == mark and board[1] == mark)
    )

# Check if the board is full
def check_tie(board):
    return ' ' not in board[1:]

# Play the game
def play_game():
    board = [' '] * 10
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board(board)
        position = int(input('Choose a position (1-9): '))

        if board[position] == ' ':
            board[position] = current_player

            if check_win(board, current_player):
                display_board(board)
                print(f'Player {current_player} wins!')
                game_over = True
            elif check_tie(board):
                display_board(board)
                print('The game is a tie!')
                game_over = True
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
        else:
            print('That position is already filled. Try again.')

# Start the game
play_game()
