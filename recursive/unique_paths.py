"""
    |   |   |   |
    |   |   |   |
    |   |   |   |

    In a 3*3 metric, start at (0,0). In each iteration you have a choice.
    you can either go right or you can go down.
    recurse on the choices.

"""

def unique_path_rec(x, y, end_x, end_y, curr_path, all_paths):
    if (x == end_x-1) and (y == end_y-1):
        all_paths.add("->".join([str(path[0])+","+str(path[1]) for path in curr_path]))
        return
    #go right
    if y < end_y:
        unique_path_rec(x=x, y=y+1, end_x=end_x, end_y=end_y,
                        curr_path=curr_path+[(x, y+1)], all_paths=all_paths)
    #go down
    if x < end_x:
        unique_path_rec(x=x+1, y=y, end_x=end_x, end_y=end_y,
                        curr_path=curr_path+[(x+1, y)], all_paths=all_paths)


def unique_paths(m, n):
    if m <= 0 or n <= 0:
        return 0
    x = 0
    y = 0
    end_x = m
    end_y = n
    curr_path = []
    all_paths = set()
    unique_path_rec(x=x, y=y, end_x=end_x, end_y=end_y, curr_path=curr_path, all_paths=all_paths)
    return all_paths


if __name__=="__main__":
    m = 3
    n = 3

    print unique_paths(m, n)