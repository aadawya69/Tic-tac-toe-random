def print_board(board):
    print(f"{board[7]}|{board[8]}|{board[9]}")
    print("-+-+-")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print("-+-+-")
    print(f"{board[1]}|{board[2]}|{board[3]}")

def check_win(board, mark):
    wins = [(7,8,9),(4,5,6),(1,2,3),
            (7,4,1),(8,5,2),(9,6,3),
            (7,5,3),(9,5,1)]
    return any(board[a]==board[b]==board[c]==mark for a,b,c in wins)

def is_board_full(board):
    return all(space != ' ' for space in board.values())

def tic_tac_toe():
    board = {i: ' ' for i in range(1,10)}
    current, other = 'X', 'O'
    while True:
        print_board(board)
        move = int(input(f"Player {current}, choose 1–9: "))
        if board.get(move) == ' ':
            board[move] = current
        else:
            print("Spot taken; try again.")
            continue
        if check_win(board, current):
            print_board(board)
            print(f" Player {current} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        current, other = other, current
    if input("Play again? (y/n): ").lower().startswith('y'):
        tic_tac_toe()

if __name__ == "__main__":
    tic_tac_toe()
