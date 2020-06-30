# supplementary function
def row_ini():
    '''
    Initialize board matrix
    '''
    global row1, row2, row3

    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']

def empty_line():
    '''
    Insert empty line below
    '''
    print()

def up_count(count):
    '''
    Count +1
    '''
    count += 1

    return count

def make_column(row1, row2, row3):
    '''
    Rows are transformed to columns
    '''
    # define col1, col2, col3
    col1 = list(range(3))
    col2 = list(range(3))
    col3 = list(range(3))
    # column1
    col1[0] = row1[0]
    col1[1] = row2[0]
    col1[2] = row3[0]
    # column2
    col2[0] = row1[1]
    col2[1] = row2[1]
    col2[2] = row3[1]
    # column3
    col3[0] = row1[2]
    col3[1] = row2[2]
    col3[2] = row3[2]

    return col1, col2, col3

def make_diagonal(row1, row2, row3):
    '''
    Rows are transformed to diagonals
    '''
    # define dia_lr, dia_rl
    dia_lr = list(range(3))
    dia_rl = list(range(3))
    # lr: left to right
    dia_lr[0] = row1[0]
    dia_lr[1] = row2[1]
    dia_lr[2] = row3[2]
    # rl: right to left
    dia_rl[0] = row1[2]
    dia_rl[1] = row1[1]
    dia_rl[2] = row1[0]

    return dia_lr, dia_rl

# main function
def display_intro():

    # displaying intro
    print('Hi, welcome to the game Tic Tac Toe!')

    # setting up variable for the while loop
    condition = False

    # while loop: choosing types of input
    while condition == False:

        user_input = input('Which do you want to be? X or O? ')

        # if the user gives wrong input, ask again
        if user_input not in ['X', 'O']:

            condition = False
            print('Error: type X or O please!')

        else:
            # print who is going to be the first
            if user_input == 'X':
                print('You are going to go First!')
                user_order = 0;

            elif user_input == 'O':
                print('You are going to go Second!')
                user_order = 1;

            # anyway the condition is true
            condition = True

    # return: user_order :: 0 for first, 1 for second
    return user_order

def display_rule():
    # board variables
    row1 = ['7', '8', '9']
    row2 = ['4', '5', '6']
    row3 = ['1', '2', '3']

    # announcement
    print('For your reference, we will teach you some rules')
    print('Below is the configuration of the board\n')

    # show configuration of the board
    print(row1)
    print(row2)
    print(row3)
    empty_line()

    # announcement(2)
    print('When you type in number, we will place your X or O based on the number')

def show_current(row1, row2, row3, count):
    # show current board on the screen
    print(f'The current situation at time {count} is: \n')

    print(row1)
    print(row2)
    print(row3)

def user1_input(row1, row2, row3):
    # we should update user1 input
    # user1 input is 'X'
    condition = 'check'

    # for user1 input to be in the range of (1-9)
    while condition not in range(1):

        user1_input = int(input('USER1:: Which position are you going to place? '))

        if user1_input in range(10):

            # if user1 input is in row1 range
            if user1_input in range(1,4):

                if row3[user1_input-1] == 'O' or row3[user1_input-1] == 'X':
                    condition = 2
                    print('That cell is occupied, please type in another number to spot!')

                else:
                    row3[user1_input-1] = 'X'
                    condition = 0

            # if user1 input is in row2 range
            if user1_input in range(4,7):

                if row2[user1_input-4] == 'O' or row2[user1_input-4] == 'X':
                    condition = 2
                    print('That cell is occupied, please type in another number to spot!')

                else:
                    row2[user1_input-4] = 'X'
                    condition = 0

            # if user1 input is in row3 range
            if user1_input in range(7,10):

                if user1_input in range(7,10):

                    if row1[user1_input-7] == 'O' or row1[user1_input-7] == 'X':
                        condition = 2
                        print('That cell is occupied, please type in another number to spot!')

                    else:
                        row1[user1_input-7] = 'X'
                        condition = 0

        else:
            condition = 2
            print('Please type number between 0 and 9')

def user2_input(row1, row2, row3):
    # we should update user2 input
    # user2 input is 'O'
    condition = 'check'

    # for user2 input to be in the range of (1-9)
    while condition not in range(1):

        user2_input = int(input('USER2:: Which position are you going to place? '))

        if user2_input in range(10):

            # if user1 input is in row1 range
            if user2_input in range(1,4):

                if row3[user2_input-1] == 'O' or row3[user2_input-1] == 'X':
                    condition = 2
                    print('That cell is occupied, please type in another number to spot!')

                else:
                    row3[user2_input-1] = 'O'
                    condition = 0

            # if user1 input is in row2 range
            if user2_input in range(4,7):

                if row2[user2_input-4] == 'O' or row2[user2_input-4] == 'X':
                    condition = 2
                    print('That cell is occupied, please type in another number to spot!')

                else:
                    row2[user2_input-4] = 'O'
                    condition = 0

            # if user1 input is in row3 range
            if user2_input in range(7,10):

                if user2_input in range(7,10):

                    if row1[user2_input-7] == 'O' or row2[user2_input-7] == 'X':
                        condition = 2
                        print('That cell is occupied, please type in another number to spot!')

                    else:
                        row1[user2_input-7] = 'O'
                        condition = 0

        else:
            condition = 2
            print('Please type number between 0 and 9')

def check_eod_user1(row1, row2, row3):
    # check to see if the game ends for user1
    # variables: col, diagonal
    # make column, diagonal
    col1, col2, col3 = make_column(row1, row2, row3)
    dia_lr, dia_rl = make_diagonal(row1, row2, row3)

    # case1: user1 wins
    # horizontal win
    if row1.count('X') == 3 or row2.count('X') == 3 or row3.count('X') == 3:
        empty_line()
        print('Player1 wins the game, CONGRAGULATION!')
        eod = True
    # vertical win
    elif col1.count('X') == 3 or col2.count('X') == 3 or col3.count('X') == 3:
        empty_line()
        print('Player1 wins the game, CONGRAGULATION!')
        eod = True
    # diagonal win
    elif dia_lr.count('X') == 3 or dia_rl.count('X') == 3:
        empty_line()
        print('Player1 wins the game, CONGRAGULATION!')
        eod = True
    else:
        empty_line()
        print('Next Person!')
        eod = False

    return eod

def check_eod_user2(row1, row2, row3):
    # check to see if the game ends for user2
    # variables: col, diagonal
    # make column, diagonal
    col1, col2, col3 = make_column(row1, row2, row3)
    dia_lr, dia_rl = make_diagonal(row1, row2, row3)

    # case2: user2 wins
    # horizontal win
    if row1.count('O') == 3 or row2. count('O') == 3 or row3.count('O') == 3:
        empty_line()
        print('Player2 wins the game, CONGRAGULATION!')
        eod = True
    # vertical win
    elif col1.count('O') == 3 or col2. count('O') == 3 or col3.count('O') == 3:
        empty_line()
        print('Player2 wins the game, CONGRAGULATION!')
        eod = True
    # diagonal win
    elif dia_lr.count('O') == 3 or dia_rl.count('O') == 3:
        empty_line()
        print('Player2 wins the game, CONGRAGULATION!')
        eod = True
    else:
        empty_line()
        print('Next Person!')
        eod = False

    return eod

def play_again():
    '''
    More games?
    '''
    more = 'ini'

    while more not in ['y', 'n']:

        more = input('Do you want to play again? (y, n)')

    return more

#### Main!! ####
def main():
    # import clear_output
    from IPython.display import clear_output
    # This is the game "Tic Tac Toe"
    # Welcome!
    # This is the main function of the program
    # turn_off_game: this is the parameter for 'keep playing: 1' or 'not: 0'
    turn_off_game = 1
    while turn_off_game != 0:

        ### define variables
        # 0.1 define board matrix
        row1 = [' ', ' ', ' ']
        row2 = [' ', ' ', ' ']
        row3 = [' ', ' ', ' ']
        # 0.2 define some variables
        count = 0
        eod = False

        # 1.1 show intro of the game Tic Tac Toe
        display_intro()
        empty_line()

        # 1.2 show rule
        display_rule()

        # 1.3 show current status at ground level
        show_current(row1, row2, row3, count)
        empty_line()

        # 2. (user input)-(update & display)-(check if the game ends)
        while eod == False:

            # user1 input
            user1_input(row1, row2, row3)
            count = up_count(count)
            clear_output()
            show_current(row1, row2, row3, count)
            eod = check_eod_user1(row1, row2, row3)
            empty_line()

            if eod == True:
                break

            # user2_input
            user2_input(row1, row2, row3)
            count = up_count(count)
            clear_output()
            show_current(row1, row2, row3, count)
            eod = check_eod_user2(row1, row2, row3)
            empty_line()

        # 3. Closing sentence
        print('Thank you for your participation!')
        print(f"Your game ended in time: '{count}'")
        empty_line()

        # 4. Play again?
        ans = play_again()
        empty_line()
        # choice
        if ans == 'y':
            # yes
            turn_off_game = 1
            print('New Game!')
        else:
            # no
            turn_off_game = 0
            print('FAREWELL!!')

main()

