import os
import random

#def clearer for console output
clear_output = lambda: os.system('cls')

def display_board(board):
    print(' {} | {} | {}'.format(board[7],board[8],board[9]))
    print('-----------')
    print(' {} | {} | {}'.format(board[4],board[5],board[6]))
    print('-----------')
    print(' {} | {} | {}'.format(board[1],board[2],board[3]))
    print('\n')

def player_input():
    marker = input('You need to choose your marker - X or O: ')
    
    while not (marker.upper() == 'X' or marker.upper() == 'O'):
        clear_output()
        marker = input(f'Your input was {marker}. Enter your marker - X or O: ')
    if marker.upper() == 'X':
        return ('X', 'O')
    elif marker.upper() == 'O':
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    if random.randint(0,1) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False

def full_board_check(board):
    count = 0
    for i in board:
        if i == ' ' or i == '':
            count+=1
    if count > 0:
        return False
    else:
        return True

def player_choice(board):
    choice = input('Enter number in range from 1 to 9(check is your cell where you want to place marker is clear): ')

    while not(choice.isnumeric() == True and int(choice) <= 9):
        clear_output()
        display_board(board)
        choice = input('Somehow your input is`t right. Try again: ')
    
    s = space_check(board, int(choice))
    while not(s == True and choice.isnumeric()==True and int(choice)<=9):
        clear_output()
        display_board(board)
        choice = input(f'Your input is not clear. Try other one: ')
        if int(choice) <= 9:
            s = space_check(board, int(choice))
    return int(choice)

def replay():
    repl = input('Do you want to play again( Yes | No ): ')

    while not(repl[0].lower()=='y' or repl[0].lower()=='n'):
        repl = input("Actually didnt catch what you said. Enter yes or no pls: ")
    if repl[0].lower() == 'y':
        return True
    else:
        return False

while True:
    clear_output()
    print('\nWelcome to Tic Tac Toe game!!!\n')

    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    hint_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    first_player = choose_first()
    print(f'{first_player} will go first\n')
    pl1, pl2 = player_input()

    play = input('\nAre you ready to play? (y/n): ')
    while not(play.lower()[0] == 'y' or play.lower()[0] == 'n'):
        play = input("Cant undestand you. Enter yes or no: ")

    if play.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        clear_output()
        if first_player == 'Player 1':
            print('Play board:\n')
            display_board(board)
            print('Hint board:\n')
            display_board(hint_board)
            position = player_choice(board)
            place_marker(board, pl1, position)

            if win_check(board, pl1):
                clear_output()
                display_board(board)
                print(f'{pl1} wins!')
                game_on = False
            else:
                if full_board_check(board):
                    clear_output()
                    display_board(board)
                    print('Its draw!')
                    break
                else:
                    first_player = 'Player 2'
        else:

            print('Play board:\n')
            display_board(board)
            print('Hint board:\n')
            display_board(hint_board)
            position = player_choice(board)
            place_marker(board, pl2, position)

            if win_check(board, pl2):
                clear_output()
                display_board(board)
                print(f'{pl2} wins!')
                game_on = False
            else:
                if full_board_check(board):
                    clear_output()
                    display_board(board)
                    print('Its draw!')
                    break
                else:
                    first_player = 'Player 1'
    if not replay():
        break

