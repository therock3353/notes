'''
    https://leetcode.com/problems/sudoku-solver/
    General approach is that recurse on each cell, if the cell has number,
    recurse to the next cell. If the cell is empty then we can place
    9 numbers there 1-9. For each of this choice recurse.

    If you reach end of row (col+1>=len(board[0])
    then go to next row. Once you reach end of rows, return (base condition).

    This is NP Complete problem. O(N) would be k^10 where there are k blank spots.

    The solution is not working, will fix it later :)
'''
import copy

class Solution(object):
    def validateSubMatrix(self, r_id, c_id, ROW_MAX, COL_MAX, board, num):
        for row_id in range(r_id, ROW_MAX):
            for col_id in range(c_id, COL_MAX):
                if num == board[row_id][col_id]:
                    return False
        return True

    def canPlaceInRow(self, r_id, c_id, board, num):
        for col_id in range(len(board[0])):
            if num == board[r_id][col_id]:
                return False
        return True

    def canPlaceInCol(self, r_id, c_id, board, num):
        for row_id in range(len(board)):
            if num == board[row_id][c_id]:
                return False
        return True

    def canPlace(self, row_id, col_id, num, board):
        result = self.canPlaceInRow(row_id, col_id, board, num)
        if result is False:
            return False
        result = self.canPlaceInCol(row_id, col_id, board, num)
        if result is False:
            return False

        if row_id < 3:
            row_id = 0
            ROW_MAX = 3
        if row_id >= 3 and row_id < 6:
            row_id = 3
            ROW_MAX = 6
        if row_id >= 6 and row_id < 9:
            row_id = 6
            ROW_MAX = 9
        if col_id < 3:
            col_id = 0
            COL_MAX = 3
        if col_id >= 3 and col_id < 6:
            col_id = 3
            COL_MAX = 6
        if col_id >= 6 and col_id < 9:
            col_id = 6
            COL_MAX = 9
        result = self.validateSubMatrix(row_id, col_id, ROW_MAX, COL_MAX, board, num)
        if result is False:
            return False
        return True

    def dfs(self, row_id, col_id, board, result):
        if row_id >= len(board):
            result = copy.deepcopy(board)
            return True
        if col_id >= len(board[0]):
            return self.dfs(row_id+1, 0, board, result)

        if board[row_id][col_id] == ".":
            for i in range(1, 10):
                if self.canPlace(row_id=row_id, col_id=col_id, num=i, board=board) is True:
                    board[row_id][col_id] = i
                    res = self.dfs(row_id, col_id+1, board, result)
                    if res is True:
                        return res
                    board[row_id][col_id] = "."
        else:
            self.dfs(row_id, col_id+1, board, result)

    def solveSudoku(self, board):
        result = []
        result = self.dfs(0, 0, board, result)
        return result


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]
         ]
print(Solution().solveSudoku(board))
