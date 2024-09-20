def print_board(board):
    size = len(board)
    for row in board:
        print(" | ".join(row))
        print("-" *(size*3-1))
def checkwinner(board,player):
    size = len(board)

#check row and column
    for i in range(size): 
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(size)]): 
            return True

#check diagonal 
    if all([board[i][i] == player for i in range(size)])or all([board[i][size -i-1] == player for i in range(size)]):
        return True 
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def tictactoe(size): 
    board = [[" " for _ in range(size)] for _ in range(size)] 
    players = ["X" , "O"] 
    Currentplayer = 0

    while True:
        print_board(board)
        row = int(input(f"player {players[Currentplayer]}, enter row (1-{size}):")) -1
        column = int(input(f"player {players[Currentplayer]}, enter column (1-{size}): ")) -1 
    
        if 0 <= row < size and 0 <= column < size:
            if board[row][column] == " ":
                board[row][column] = players[Currentplayer]
                
                if checkwinner(board,players[Currentplayer]):
                    print_board(board)
                    print(f"player{players[Currentplayer]} wins!")
                    break
                elif is_draw(board):
                    print_board(board)
                    print("it is a tie!")
                    break
            
                Currentplayer = 1 - Currentplayer
            else:
                print("cell already taken try again.")
        else:
              print("Invalid move. Please enter values within the board size.")
        
size = int(input("enter the size of tictactoe board(eg. 3 for 3*3 ,4 for 4*4):"))

tictactoe(size)
          