from queue import Queue

def traverse_island_bfs(row_id, col_id, A, visited):
    queue = Queue()
    queue.put((row_id, col_id))
    while not queue.empty():
        item = queue.get()
        row_id = item[0]
        col_id = item[1]
        if row_id > 0 and A[row_id-1][col_id] == 1 and (row_id-1, col_id) not in visited:
            queue.put((row_id-1, col_id))
        if col_id < len(A[0])-1 and A[row_id][col_id+1] == 1 and (row_id, col_id+1) not in visited:
            queue.put((row_id, col_id+1))
        if col_id > 0 and A[row_id][col_id-1] == 1 and (row_id, col_id-1) not in visited:
            queue.put((row_id, col_id-1))
        if row_id < len(A)-1 and A[row_id+1][col_id] == 1 and (row_id+1, col_id) not in visited:
            queue.put((row_id+1, col_id))
        visited.add((row_id, col_id))


def traverse_island_dfs(row_id, col_id, A, visited):
    if A[row_id][col_id] != 1 or (row_id, col_id) in visited:
        return
    visited.add((row_id, col_id))
    #go right
    if col_id < len(A[0])-1:
        traverse_island_dfs(row_id, col_id+1, A, visited)
    #go left
    if col_id > 0:
        traverse_island_dfs(row_id, col_id-1, A, visited)
    #go up
    if row_id > 0:
        traverse_island_dfs(row_id-1, col_id, A, visited)
    #go down
    if row_id < len(A)-1:
        traverse_island_dfs(row_id+1, col_id, A, visited)


def num_of_islands(A, algo='dfs'):
    num_islands = 0
    visited = set()
    for row_id in range(len(A)):
        for col_id in range(len(A[0])):
            if A[row_id][col_id] == 1 and (row_id, col_id) not in visited:
                if algo == 'dfs':
                    traverse_island_dfs(row_id, col_id, A, visited)
                else:
                    traverse_island_bfs(row_id, col_id, A, visited)
                num_islands += 1

    return num_islands


if __name__=="__main__":
    A = [
            [0, 1, 1, 0, 0, 1],
            [0, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
    ]
    print(num_of_islands(A, algo='dfs'))
    print(num_of_islands(A, algo='bfs'))
