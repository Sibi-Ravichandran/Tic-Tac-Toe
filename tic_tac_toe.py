# Title:    Two Player Tic Tac Toe Game 
# Description: The script takes the inputs 'X' and 'O' from two players and decides who is the winner. 
# Author: Sibi Ravichandran
# Date: 08-June-2020

# Function to display the key options to the players: 
def keyoptions(): 
    print ('')
    print ('The players can enter the following number keys to fill the respective squares: ') 
    print (' 7 | 8 | 9 ')
    print ('---|---|---')
    print (' 4 | 5 | 6 ')
    print ('---|---|---')
    print (' 1 | 2 | 3 ')
    print ('')   

# Function to display the board to the players:
def display_board(board):
    print ('')   
    print (' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print ('---|---|---')
    print (' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print ('---|---|---')
    print (' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print ('')        

# Function to assign markers 'X' and 'O' to players:   
def assign_markers():
    marker = input("Player-1 do you want to be 'X' or 'O': ").upper()
    if marker=='X': 
        return ('X', 'O')
    else:
        return ('O', 'X')
 
# Function to fill the board with the player inputs: 
def place_marker(board, marker, position):
    board[position] = marker
 
# Function to check the winning criteria:  
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Function to check if the position to be filled is empty or not: 
def space_check(board, position):
    return board[position] == ' '

# Function to check if the entire board is full or not:
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Function to choose which player should go first randomly: 
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function to ask the position from the player:
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))       
    return position

# Function to ask for a re-match:
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# The main part: 

while True: 
    print ('#######################')
    print ('Welcome to Tic Tac Toe!')
    print ('#######################')
    
    # Reset the board: 
    gameboard=[' ']*10;
    # Assign markers to the players:
    p1_marker, p2_marker = assign_markers()
    print ("Player-1 chose " +p1_marker)
    print ("Player-2 chose " +p2_marker)
    # Choose who will go first:
    turn=choose_first();
    print (turn+ ' will go first')
    # Display the key opetions:
    keyoptions()
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(gameboard)
            position = player_choice(gameboard)
            place_marker(gameboard, p1_marker, position)

            if win_check(gameboard, p1_marker):
                display_board(gameboard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(gameboard)
            position = player_choice(gameboard)
            place_marker(gameboard, p2_marker, position)

            if win_check(gameboard, p2_marker):
                display_board(gameboard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(gameboard):
                    display_board(gameboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break  

###########################################################################################################################        