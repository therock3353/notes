'''
    You are given a m*n matrix of 0 and 1 and a starting point (x,y).
    You need to flip all the 'adjacent cubes' of starting point. i.e if
    starting point was 0 then all it's adjacent cubes who are 0, must be turned to 1
'''
from queue import Queue

def paint_matrix_bfs(A, x, y):
    if A[x][y] == 1:
        val_to_flip = 1
        flipped_val = 0
    else:
        val_to_flip = 0
        flipped_val = 1

    visited = set()
    q = Queue()
    q.put((x, y))
    while not q.empty():
        item = q.get()
        x = item[0]
        y = item[1]
        A[x][y] = flipped_val
        if x > 0 and A[x-1][y] == val_to_flip and (x-1, y) not in visited:
            q.put((x-1, y))
        if y < len(A[0])-1 and A[x][y+1] == val_to_flip and (x, y+1) not in visited:
            q.put((x, y+1))
        if x < len(A)-1 and A[x+1][y] == val_to_flip and (x+1, y) not in visited:
            q.put((x+1, y))
        if y > 0 and A[x][y-1] == val_to_flip and (x, y-1) not in visited:
            q.put((x, y-1))

        visited.add((x, y))


def paint_matrix_dfs(A, x, y):
    pass


if __name__=="__main__":

    A = [[1, 1, 0, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 1, 1],
         [1, 1, 1, 1, 0],
         [1, 1, 0, 0, 0]]

    paint_matrix_bfs(A, x=1, y=4)
    for row in range(len(A)):
        print(A[row])
    # paint_matrix_dfs(A, x=2, y=1)
    # print(A)