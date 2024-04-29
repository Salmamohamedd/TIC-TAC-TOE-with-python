# TIC TAC TOE game with Python
#### Video Demo:  <https://youtu.be/DyKAKi7tuGo?si=YNySBtNoJyKzbaNk>
#### Description:
This is a Python implementation of a tic-tac-toe game that allows a user to play against either a random computer player or an AI player.
Here's an explanation of the code:

Imports: The code imports the tabulate module for displaying the game board and the random module for generating random numbers.

Global Variables: There are two global lists, board and marks, that store the numbers 1-9 and the corresponding X or O marks for each cell on the board.

Function main(): This is the entry point of the program. It takes the user's name and choice of opponent, and then calls the playRandom() or playAI() function accordingly.

Function playRandom(): This function allows the user to play against a random computer player. It displays the board, takes the user's input, updates the board, checks for winners, and then repeats the process for the random computer player.It also handles exception that may result from the user while choosing an invalid cell.

Function playAI(): This function allows the user to play against an AI player. It works similarly to playRandom(), but instead of generating a random number for the AI player's move, it uses a bestMove() function to find the optimal move based on the minimax algorithm.

Function check_winner(): This function checks if there are any winning combinations on the board. It returns the winning combination as a string or 0 if there are no winners.

Function all_empty(): This function checks if all the cells on the board are empty. It returns True if there are no empty cells.

Function check_state(): This function checks the state of the board and returns 2 if X has won, -2 if O has won, 0 if there is a tie, and 1 if the game is still ongoing.

Function bestMove(): This function uses the minimax algorithm to find the optimal move for the AI player. It iterates over all the empty cells on the board and recursively calls the minimax() function to simulate the game for each move. It then returns the move that results in the best score.

Function minimax(): This function is the core of the AI player's strategy. It uses recursion and backtracking to simulate the game for the current board state and returns the score for the maximizing player (X) or the minimizing player (O).

Function modify_board(): This function updates the marks list with the corresponding X or O marks for each cell on the board.

Function display_board(): This function displays the board using the tabulate module.


Here are the steps on how to play:

Enter your name and choose your opponent (random computer player or AI player).
Choose a cell by entering its number.
The game will display the board after each move.
The game will announce the winner or declare a tie when the game is over.