import random


def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def winner(theBoard):
    if (theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R']) and theBoard['top-R'] != ' ':
        return True
    elif (theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R']) and theBoard['mid-R'] != ' ':
        return True
    elif (theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R']) and theBoard['low-R'] != ' ':
        return True
    elif (theBoard['low-L'] == theBoard['mid-M'] == theBoard['top-R']) and theBoard['top-R'] != ' ':
        return True
    elif (theBoard['low-R'] == theBoard['mid-M'] == theBoard['top-L']) and theBoard['top-L'] != ' ':
        return True
    elif (theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R']) and theBoard['mid-R'] != ' ':
        return True
    elif (theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L']) and theBoard['low-L'] != ' ':
        return True
    elif (theBoard['low-M'] == theBoard['mid-M'] == theBoard['top-M']) and theBoard['top-M'] != ' ':
        return True
    elif (theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R']) and theBoard['low-R'] != ' ':
        return True
    else:
        return False


# Start of the game (program). By default, we start playing because again = y
again = 'y'
while again == 'y':
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    turn = 'X'

    # Now, we ask for the mode. mode = 1 -> against computer, mode = 2 -> 2 players
    mode = int(input("How many players for this game? [1-2]"))
    # enter mode

    # Loop to ask for actual spots on the current game
    for i in range(9):
        printboard(theBoard)  # Prints the current state of board
        # If mode 1, the computer makes a random choice between the possible spots
        if mode == 1 and turn == 'O':
            move = random.choice(list(theBoard.keys()))
            # If mode 2, we ask the next player for the move
        else:
              print('Turn for ' + turn + '. Move on which space?')
              move = input()

        while move not in theBoard or theBoard[move] != ' ':  # if not valid value for not in
            print("Spot is not valid")
            if mode == 1:
                move = random.choice(list(theBoard.keys()))
            else:
                move = input()

                theBoard[move] = turn  # Assign current move to the player in turn
                if winner(theBoard):
                    print(turn + ' is the winner')
            break  # Breaks the current for-loop for the actual game
        if turn == 'X':
            turn = 'O'

        else:
            turn = 'X'

    # Once the current game is over (for-loop in 45), we ask the player if he wants
    # to playe once again
    print('Do you want to play again? Y/N')
    again = input()
    # If Y, we just continue with the next loop to start a new game
    if again != 'N':
        continue
    else:  # If not, we break the main while loop (line 34), to stop the program
        break

    printboard(theBoard)
    # play again