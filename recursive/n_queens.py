import copy


def up(board, x, y):
    result = True
    if x < 0:
        return result
    if board[x][y] == -1:
        return False
    result = up(board, x-1, y)
    return result

def down(board, x, y):
    result = True
    if x >= len(board):
        return result
    if board[x][y] == -1:
        return False
    result = down(board, x+1, y)
    return result

def left(board, x, y):
    result = True
    if y < 0:
        return result
    if board[x][y] == -1:
        return False
    result = left(board, x, y-1)
    return result

def right(board, x, y):
    result = True
    if y >= len(board[0]):
        return result
    if board[x][y] == -1:
        return False
    result = right(board, x, y+1)
    return result

def left_up(board, x, y):
    result = True
    if x < 0 or y < 0:
        return result
    if board[x][y] == -1:
        return False
    result = left_up(board, x-1, y-1)
    return result

def left_down(board, x, y):
    result = True
    if x >= len(board) or y < 0:
        return result
    if board[x][y] == -1:
        return False
    result = left_down(board, x+1, y-1)
    return result

def right_up(board, x, y):
    result = True
    if x < 0 or y >= len(board[0]):
        return result
    if board[x][y] == -1:
        return False
    result = right_up(board, x-1, y+1)
    return result

def right_down(board, x, y):
    result = True
    if x >= len(board) or y >= len(board[0]):
        return result
    if board[x][y] == -1:
        return False
    result = right_down(board, x+1, y+1)
    return result

def is_queen_placement_valid(board, x_pos, y_pos):

    if up(board, x_pos-1, y_pos) is False:
        return False
    if down(board, x_pos+1, y_pos) is False:
        return False
    if left(board, x_pos, y_pos-1) is False:
        return False
    if right(board, x_pos, y_pos+1) is False:
        return False
    if left_up(board, x_pos-1, y_pos-1) is False:
        return False
    if left_down(board, x_pos+1, y_pos-1) is False:
        return False
    if right_up(board, x_pos-1, y_pos+1) is False:
        return False
    if right_down(board, x_pos+1, y_pos+1) is False:
        return False
    return True
'''
board =    
    [
        [0,-1,0,0],
        [-1,0,0,-1],
        [0,0,0,0],
        [0,-1,0,0]
    ]
we need to check if the board is valid. i.e queens are not attacking each other.
'''
def is_valid_chessboard(board):
    is_valid = False
    for row_id in range(len(board)):
        for col_id in range(len(board[0])):
            if board[row_id][col_id] == -1:
                if not is_queen_placement_valid(board, row_id, col_id):
                    return is_valid

    is_valid = True
    return is_valid

"""
    The optimization is that if there is a 4*4 board then all queens must be on
    different rows. We can select the position of 1st queen in 4 ways. 1 in 4 ways for 4 different times.
    and if there are 4 rows then each row can have 4 possibilities of queen placement
    hence the O(n) = 4 ^ 4 = 256. This is much better than 4C16 (which is 1820).
    
    [0, 0, q, 0] => queen can be placed anywhere from 0-3 index so there are 4 possibilities
    [q, 0, 0, 0] => since queen can be placed anywhere from 0-3 on this row as well, the total possibilities between row 0 and 1 = 4*4 = 16
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    
    After each complete possibility, the board becomes complete and must be evaluated if this is a valid board or not.
    
"""
def n_queens_brute_force(board, num_queens, result, result_cntr):
    if num_queens == 0:
        result_cntr["r"] += 1
        if is_valid_chessboard(board=board):
            s = ""
            for i in range(len(board)):
                for j in range(len(board[0])):
                    s+=str(board[i][j])
            if s not in result:
                result[s] = board
                print "=== valid chessboard ==="
                for i in range(len(board)):
                    print board[i]
        return

    for index in range(len(board[0])):
        if board[num_queens-1][index] == 0:
            new_board = copy.deepcopy(board)
            new_board[num_queens-1][index] = -1
            n_queens_brute_force(board=new_board, num_queens=num_queens-1, result=result, result_cntr=result_cntr)


if __name__=="__main__":
    b = [
        [0, 0, 0 ,0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    num_queens = 4
    cntr = {"r": 0}
    n_queens_brute_force(board=b, num_queens=num_queens, result={}, result_cntr=cntr)
    print "cntr {}".format(cntr)