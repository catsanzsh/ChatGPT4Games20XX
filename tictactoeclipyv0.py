import os

# Tic Tac Toe game in Python

def print_board(board):
  for i in range(3):
    print('|', end='')
    for j in range(3):
      print(board[i][j], end=' |')
    print('\n---------')

def check_win(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != ' ':
      return True
    if board[0][i] == board[1][i] == board[2][i] != ' ':
      return True
  if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
    return True
  return False

def tic_tac_toe():
  """
  Runs a simple command-line Tic-Tac-Toe game for two players.

  The game board is a 3x3 grid, and players take turns to place their marks ('X' or 'O') on the board.
  The game continues until one player wins or the board is full.

  The function does the following:
  1. Initializes an empty 3x3 game board.
  2. Alternates turns between Player 'X' and Player 'O'.
  3. Prompts the current player to enter their move (row and column).
  4. Validates the move and updates the board.
  5. Checks if the current player has won after each move.
  6. Declares the winner and ends the game if a player wins.

  Note:
  - The players are prompted to enter their moves as row and column indices (0, 1, or 2).
  - If a player attempts to place their mark on an already occupied cell, they are prompted to try again.

  Returns:
    None
  """
  board = [[' ' for _ in range(3)] for _ in range(3)]
  current_player = 'X'
  while True:
    print_board(board)
    while True:
      move_row = int(input('Enter the row for your move (0, 1, or 2): '))
      move_col = int(input('Enter the column for your move (0, 1, or 2): '))
      if board[move_row][move_col] == ' ':
        board[move_row][move_col] = current_player
        break
      print('Invalid move, try again.')
    if check_win(board):
      print('Player', current_player, 'wins!')
      break
    current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
