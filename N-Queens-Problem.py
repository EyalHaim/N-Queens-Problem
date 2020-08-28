##############Version 1 of the problem###########################

#Given a chess board of size N*N containing only dragons, returns how many
#legal ways exist to locate N queens on the board

def queens_dragons(board):
    return queens_dragons_rec(len(board), 0, 0, board)

def queens_dragons_rec(remaining, row, col, board):
  if remaining == 0:
      return 1
  else:
      counter = 0
  for c in range(col, len(board)):
      for r in range(row, len(board)):
          if r != len(board) - 1:
              if legal_dragons(board, r, c):
                  board[r][c] = "Q"
                  counter += queens_dragons_rec(remaining - 1, r + 1, c, board)
                  board[r][c] = " "
          else:
              if legal_dragons(board, r, c):
                  board[r][c] = "Q"
                  counter += queens_dragons_rec(remaining - 1, 0, c + 1, board)
                  board[r][c] = " "
      row = 0
  return counter

def legal_dragons(board, row, col):
    n=len(board)
    if board[row][col] != " ":
        return False
    for j in range(col, -1, -1): #Check row to left
        if board[row][j] == "D":
            break
        if board[row][j] == "Q":
            return False

    for i in range(row, -1, -1): #Check col to up
        if board[i][col] == "D":
            break
        if board[i][col] == "Q":
            return False

    for i in range(1, n): #check left+up diagonal
        if (row-i) < 0 or (col-i) < 0:
            break
        if board[row-i][col-i] == "D":
            break
        if board[row-i][col-i] == "Q":
            return False

    for i in range(1, n): #check left+down diagonal
        if (row+i) > (n-1) or (col-i) < 0:
            break
        if board[row+i][col-i] == "D":
            break
        if board[row+i][col-i] == "Q":
            return False
    return True

##############Version 2 of the problem###########################

#Given a positive number n, returns how many legal chess boards (without dragons) of size NXN  
#can contain N queens
def queens(n):
    board = [[" " for i in range(0, n)] for i in range(0, n)]
    Queens = 0
    return recfunc(n, Queens, board)

def recfunc(n, Queens, board):
    if Queens == n:
        return 1
    else:
        counter = 0
        for j in range(n):
            if legal(board, j):
                board[Queens][j] = "Q"
                counter += recfunc(n, Queens+1, board)
                board[Queens][j] = " "
        return counter

#Returns 'True' if a Queen can be legaly placed in col 'i' and row 'j', and 'False' otherwise
def legal(partial, i):
    k=0
    for row in partial:
        if 'Q' not in row:
            j = k
            break
        k += 1
    m = 0
    for row in partial:
        if row[i] == 'Q':
            return False
        if i+(j-m) <= len(partial)-1:
            if row[i+(j-m)] == 'Q':
                return False
        if i-(j-m) >= 0:
            if row[i-(j-m)] == 'Q':
                return False
        m += 1
        if j < m:
            break
    return True
    
########
# Tester
########

def test():
    n = 5        
    empty_board = [[' ' for i in range(5)] for j in range(5)]
    if queens_dragons(empty_board) != 10:
        print("Error in queens_dragons")
    
    if queens(5) != 10:
        print("Error in queens")
    board = [[' ', ' ', 'Q', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' '], 
            [' ', 'Q ', 'D', 'Q', ' '], 
            [' ', ' ', ' ', ' ', ' '], 
            ['Q', ' ', 'D', ' ', ' ']]

    if legal_dragons(board, 2, 4) or not legal_dragons(board, 4, 4):
        print("Error in legal_dragons")
    
    board8 = [[' ', ' ', 'Q', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', 'Q', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'Q'],
             ['Q', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    if legal(board8, 1) or not legal(board8, 3):
        print("Error in legal")
        

