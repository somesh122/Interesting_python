theboard = {'7':' ' , '8':' ' , '9':' ',
            '4':' ' , '5':' ' , '6':' ',
            '1':' ' , '2':' ' , '3':' '}

board_keys =[]
for keys in theboard:
    board_keys.append(keys)

def printboard(board): #We will have to print the updated board after every move in the game and thus we will make a function in which we'll define the printBoard function so that we can easily print the board everytime by calling this function.
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn ='X'
    count =0

    for i in range(10):
        printboard(theboard)
        print("Its your turn," + turn + ".Move to which place?")

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ': # across the top
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ': # across the middle
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ': # across the bottom
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ': # down the left side
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ': # down the middle
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ': # down the right side
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ': # diagonal
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ': # diagonal
                printboard(theboard)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theboard[key] = " "

game()

#if __name__ == "__main__":
 #   game()
