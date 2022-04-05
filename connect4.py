from typing import Union

def displayBoard(board):
    for r in range(number_of_lines):
        print("____________________________")
        for c in range(number_of_columns):
            print(" " + board[r][c] + " |", end='')
            if c == number_of_columns - 1:
                print('')
    print("=" * number_of_columns * 4)
    print(' '+'   '.join(str(x) for x in range(number_of_columns)))

def locate(board, column: int) -> Union[int,None]:
    '''
    Returns the first empty row number for a given column 
     or return None if the column is full
    '''

    for r in range(number_of_lines, 0, -1):
        if board[r-1][column] == ' ':
            return r - 1
    if r == 0:
        return None

def check_winner(board, row, column) -> bool:
    '''
    Returns true if the game is won
    '''
    mark = board[row][column]
    count = 0
    # Check vertical
    for r in range(row, number_of_lines):
        if board[r][column] == mark:
            count += 1
        else:
            break
    
    if count == 4:
        return True

    count = 0
    # Check horizontal
    started = False
    for c in range(number_of_columns):
        if board[row][c] == mark:
            count += 1
            started = True
            if count == 4:
                break
        else:
            if started:
                started = False
                count = 0
    if count == 4:
        return True

    # Check diagonal

    up_left_cnt = 0
    up_right_cnt = 0
    down_left_cnt = 0
    down_right_cnt = 0
    # Top-left diagonal
    r = row
    c = column
    for x in range(4):
        if board[r][c] == mark:
            up_left_cnt += 1
        if r > 0:
            r -= 1
        else:
            break
        if c > 0:
            c -= 1
        else:
            break

    # Top-right diagonal
    r = row
    c = column
    for x in range(4):
        if board[r][c] == mark:
            up_right_cnt += 1
        if r > 0:
            r -= 1
        else:
            break
        if c < number_of_columns - 1:
            c += 1
        else:
            break

    # Down-left diagonal
    r = row
    c = column
    for x in range(4):
        if board[r][c] == mark:
            down_left_cnt += 1
        if r < number_of_lines - 1:
            r += 1
        else:
            break
        if c > 0:
            c -= 1
        else:
            break
        
    # Down-right diagonal
    r = row
    c = column
    for x in range(4):
        if board[r][c] == mark:
            down_right_cnt += 1
        if r < number_of_lines - 1:
            r += 1
        else:
            break
        if c < number_of_columns - 1:
            c += 1
        else:
            break

    if (up_left_cnt + down_right_cnt - 1 >= 4) or (up_right_cnt + down_left_cnt - 1 >= 4):
        return True
    
    return False
    
if __name__ == '__main__':

    playing = True
    number_of_columns = 7
    number_of_lines = 6
    board = [ [ ' ' for _ in range(number_of_columns)] for _ in range(number_of_lines) ]
    which_player = 1
    mark = [' ', 'X', 'O']
    displayBoard(board)

    while playing:
        
        move = input(f"Player {which_player} play, column?")
        move = int(move)
        row = locate(board, move)
        if row != None:
            board[row][move] = mark[which_player]
            playing = not check_winner(board, row, move)
            displayBoard(board)
            if not playing:
                print(f'Congratulations, Player {which_player} won!')
            which_player = 1 if which_player == 2 else 2