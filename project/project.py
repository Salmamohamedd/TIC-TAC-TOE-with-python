import tabulate
import random


def main():
    # Take the user's name
    name = input("Enter your name: ")
    # check their choice of opponent
    choice = int(input("Would you like to play with (1) a random computer player or (2) an AI player?"))
    while True:
        if choice == 1:
            playRandom(name)
            break
        elif choice == 2:
            playAI(name)
            break
        else:
            choice = int(input("Please choose a valid option: 1 for random player, 2 for an AI player"))


# board to remove cells from
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# board to put x and o on
marks = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def playRandom(name):
    while True:
        # First displaying the board and checking for winners
        display_board()
        if check_winner(marks) == "X wins":
            print("Congratulations", name, "you won!")
            break
        elif check_winner(marks) == "O wins":
            print("Random computer player won")
            break
        else:
            try:
                # Taking user's choice of cell an input
                user_choice = int(input("choose a cell: "))
                if user_choice not in board:
                    raise ValueError
                # removing user's choice of cell from board so it's not valid anymore
                board.remove(user_choice)
                # updating the marks list values
                modify_board(user_choice, 'X')
                # checking for winning
                if check_winner(marks) == 'X wins':
                    display_board()
                    print("Congratulations", name, "you won!")
                    break
                # checking for tie
                elif all_empty():
                    display_board()
                    print("It's a tie!")
                    break
                # random player's turn
                rand_choice = random.choice(board)
                # removing random player's choice of cell from board so it's not valid anymore
                board.remove(rand_choice)
                # updating the marks list values
                modify_board(rand_choice, 'O')
            except ValueError:
                # in case user chose an invalid cell
                print("cell not valid")
            except IndexError:
                # in case user played in the last cell and random player did not get a choice from board
                display_board()
                if all_empty():
                    print("It's a tie!")
                    break
                elif check_winner(marks) == "X wins":
                    print("Congratulations", name, "you won!")
                    break


def playAI(name):
    while True:
        # First displaying the board and checking for winners
        display_board()
        if all_empty():
            print("It's a tie!")
            break
        elif check_winner(marks) == "X wins":
            print("Congratulations", name, "you won!")
            break
        elif check_winner(marks) == "O wins":
            print("AI player won")
            break
        else:
            try:
                # Taking user's choice of cell as input
                user_choice = int(input("choose a cell:"))
                if user_choice not in board:
                    raise ValueError
                # removing user's choice of cell from board so it's not valid anymore
                board.remove(user_choice)
                # updating the marks list values
                modify_board(user_choice, 'X')
                #checking for tie
                if all_empty():
                    display_board()
                    print("it's a tie!")
                    break
                # checking for winning
                elif check_winner(marks) == "X wins":
                    display_board()
                    print("Congratulations", name, "you won!")
                    break
                # ai choice is the index returned from bestMove function + 1 so it would be a number that exists in marks and board lists
                ai_choice = bestMove(marks) + 1
                # removing ai player's choice of cell from board so it's not valid anymore
                board.remove(ai_choice)
                # updating the marks list values
                modify_board(ai_choice, 'O')
                # checking for winning
                if check_winner(marks) == "O wins":
                    display_board()
                    print("AI player won")
                    break
            except ValueError:
                # in case user chose an invalid cell
                print("cell not valid")
            except IndexError:
                # in case user played in the last cell and random player did not get a choice from board
                display_board()
                if all_empty():
                    print("It's a tie!")
                    break
                elif check_winner(marks) == "X wins":
                    print("Congratulations", name, "you won!")
                    break


def check_winner(marks):
    # three possibilites of row winnings
    row_win = [0] * 3
    # three possibilites of column winnings
    col_win = [0] * 3
    # 2 possibilites of diagonal winnings
    diag_win = [0, 0]
    i = 0
    for j in range(3):
        row_win[j] = marks[i] if marks[i] == marks[i + 1] == marks[i + 2] else 0
        i += 3

    for j in range(3):
        col_win[j] = marks[j] if marks[j] == marks[j + 3] == marks[j + 6] else 0

    if marks[0] == marks[4] == marks[8]:
        diag_win[0] = marks[0]
    if marks[2] == marks[4] == marks[6]:
        diag_win[1] = marks[2]
    # return 'X wins' if there's any case where X wins and 'O wins' in case O player wins
    for j in range(3):
        if row_win[j]:
            return str(row_win[j]) + ' wins'
        elif col_win[j]:
            return str(col_win[j]) + ' wins'

    for j in range(2):
        if diag_win[j]:
            return str(diag_win[j]) + ' wins'
    # return 0 if there's no winnings
    return 0


def all_empty():
    # return true only if there's no winner and no valid cells to play anymore
    return (not check_winner(marks)) and (len(board) == 0)


def check_state(marks):
    # returns 2 in case X wins, -2 in case O wins, 0 in case of a tie, and 1 otherwise(game is still ongoing)
    row_win = [0] * 3
    col_win = [0] * 3
    diag_win = [0, 0]
    i = 0
    for j in range(3):
        row_win[j] = marks[i] if marks[i] == marks[i + 1] == marks[i + 2] else 0
        i += 3

    for j in range(3):
        col_win[j] = marks[j] if marks[j] == marks[j + 3] == marks[j + 6] else 0

    if marks[0] == marks[4] == marks[8]:
        diag_win[0] = marks[0]
    if marks[2] == marks[4] == marks[6]:
        diag_win[1] = marks[2]

    for j in range(2):
        if diag_win[j] == 'X':
            return 2
        elif diag_win[j] == 'O':
            return -2

    for j in range(3):
        if row_win[j]:
            return 2 if row_win[j] == 'X' else -2

    for j in range(3):
        if col_win[j]:
            return 2 if col_win[j] == 'X' else -2

    if (not check_winner(marks)) and (all(type(mark) == str for mark in marks)):
        return 0
    return 1


def bestMove(marks):
    # initializing best_move with value 0
    best_move = 0
    # making the value of best_score as big as possible
    best_score = float('inf')
    for i in range(9):
        # iterating over every single cell in marks and checking if it's valid to play in or not
        if type(marks[i]) == int:
            # if it's valid, put O in such cell
            marks[i] = 'O'
            # get the score from playing in that cell through the recursive function minimax by making the next turn X's turn and depth is zero
            score = minimax(marks, 0, True)
            # backtrack and return the original value to that cell
            marks[i] = i + 1
            # see if the score returned from the recursive function is less than or equal to the best_score
            if score <= best_score:
                # assign best_score to the smallest value returned from minimax
                best_score = score
                # keep track of the position associated with the least value returned from minimax
                best_move = i
    # return the index associated with the least value returned from minimax
    return best_move


def minimax(marks, depth, isMax):
    # base case: check for any winnings oe tie through the check_state function
    result = check_state(marks)
    if result != 1:
        return result
    # in case of maximization: X's turn
    if isMax:
        # making best_score as small as possible because that's the maximizing case
        best_score = float('-inf')
        for i in range(9):
        # iterating over every single cell in marks and checking if it's valid to play in or not
            if type(marks[i]) == int:
                # if it's valid, put X in such cell
                marks[i] = 'X'
                # recurse after putting X but it's O's turn now so it's minimizing(isMax is False) with increasing the depth
                score = minimax(marks, depth + 1, False)
                # backtrack and return the original value to that cell
                marks[i] = i + 1
                # the new best score will be the maximum between the old best score and score returned from recursion
                best_score = max(score, best_score)
        # return the biggest value possible from recursion
        return best_score
    # in case of minimization: O's turn
    else:
        # making best_score as large as possible because that's the minimizing case
        best_score = float('inf')
        for i in range(9):
            # iterating over every single cell in marks and checking if it's valid to play in or not
            if type(marks[i]) == int:
                # if it's valid, put O in such cell
                marks[i] = 'O'
                # recurse after putting O but it's X's turn now so it's maximizing(isMax is True) with increasing the depth
                score = minimax(marks, depth + 1, True)
                # backtrack and return the original value to that cell
                marks[i] = i + 1
                # the new best score will be the minimum between the old best score and score returned from recursion
                best_score = min(score, best_score)
        # return the smallest value possible from recursion
        return best_score


def modify_board(num, symbol):
    # adding character in marks list
    marks[num - 1] = symbol


def display_board():
    # displaying marks list with tabulate module
    brd = [[marks[0], marks[1], marks[2]], [marks[3], marks[4], marks[5]], [marks[6], marks[7], marks[8]]]
    print(tabulate.tabulate(brd[0:], tablefmt="grid"))


if __name__ == "__main__":
    main()
