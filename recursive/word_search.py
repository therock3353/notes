'''
    79. Word Search
    https://leetcode.com/problems/word-search/
    If the board is of size n*n and if word length is m.
    time complexity is O(n^2 * m)

'''
def word_search_dfs(r_id, c_id, wrd_idx, visited, board, word):
    if board[r_id][c_id] != word[wrd_idx]:
        return False

    visited.add((r_id, c_id))
    if wrd_idx == len(word)-1:
        return True
    #up
    if (r_id-1 >= 0) and ((r_id-1, c_id) not in visited):
        res = word_search_dfs(r_id-1, c_id, wrd_idx+1, visited, board, word)
        if res is True:
            return res
    #down
    if (r_id+1 < len(board)) and ((r_id+1, c_id) not in visited):
        res = word_search_dfs(r_id+1, c_id, wrd_idx+1, visited, board, word)
        if res is True:
            return res
    #left
    if (c_id-1 >= 0) and ((r_id, c_id-1) not in visited):
        res = word_search_dfs(r_id, c_id-1, wrd_idx+1, visited, board, word)
        if res is True:
            return res
    #right
    if (c_id+1 < len(board[0])) and ((r_id, c_id+1) not in visited):
        res = word_search_dfs(r_id, c_id+1, wrd_idx+1, visited, board, word)
        if res is True:
            return res

    visited.remove((r_id, c_id))
    return False


def word_search(board, word):
    if not board or not word:
        return False

    visited = set()
    word_exists = False
    for row_id in range(len(board)):
        for col_id in range(len(board[0])):
            if board[row_id][col_id] == word[0]:
                word_exists = word_search_dfs(r_id=row_id, c_id=col_id, wrd_idx=0,
                                              visited=visited, board=board, word=word)
                if word_exists is True:
                    break
        if word_exists is True:
            break

    return word_exists

if __name__=="__main__":
    board = [['a', 'a', 'a'],
             ['a', 'a', 'a'],
             ['a', 'a', 'c']]
    word = 'aab'
    print(word_search(board, word))