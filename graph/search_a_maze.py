
# def search_maze_bfs(maze, x, y, visited):
#     pass

def search_maze_dfs(maze, x, y, visited):
    if x == 0 and y == (len(A[0])-1):
        print("Reached at Destination")

    if maze[x][y] == 1 or (x, y) in visited:
        return
    visited.append((x, y))
    #go right
    if y < (len(A[0])-1) and (x, y+1) not in visited:
        search_maze_dfs(maze, x, y+1, visited)
    #go up
    if x > 0 and (x-1, y) not in visited:
        search_maze_dfs(maze, x-1, y, visited)
    #go left
    if y > 0 and (x, y-1) not in visited:
        search_maze_dfs(maze, x, y-1, visited)
    #go down
    if x < (len(A)-1) and (x+1, y) not in visited:
        search_maze_dfs(maze, x+1, y, visited)
    visited.pop()

def search_maze(maze):
    x, y = 0, 0
    visited = []
    search_maze_dfs(maze=maze, x=x, y=y, visited=visited)

if __name__=="__main__":

    A = [[0, 0, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 1, 0]]

    print(search_maze(maze=A))