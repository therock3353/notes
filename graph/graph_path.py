from queue import Queue
'''
    0 -------- 2 ----------- 4
    |          |             |
    |          |             |
    1          3 ----------- 5 ---------- 6

to find path between 1 and 6

put 1 in queue      queue(1)       visited()
q.get()  #1         queue()        visited(1)
neighbours -> [0]
                    queue(0)       visited(1) 

q.get()  #0         queue()        visited(1)
neighbours->[1,2]
                    queue(2)       visited(1,0) 


q.get() #2          queue()        visited(1,0)
neighbours->[0,3,4]
                    queue(3)       visited(1,0,2) 
                    queue(3,4)     visited(1,0,2)

q.get() #3          queue(4)        visited(1,0,2)
neighbours->[2,5]
                    queue(4)       visited(1,0,2) 
                    queue(4,5)     visited(1,0,2,3)
                    
'''
def get_graph():
    graph = {
         0: [1, 2],
         1: [0],
         2: [0, 3, 4],
         3: [2, 5],
         4: [2, 5],
         5: [3, 4, 6],
         6: [5]
        }
    return graph

# using BFS
def has_path(graph, src, dest):
    q = Queue()
    q.put(src)
    visited = set()
    while not q.empty():
        node = q.get()
        if node == dest:
            return True
        visited.add(node)
        neighbours = graph.get(node, [])
        for neighbour in neighbours:
            if neighbour not in visited:
                q.put(neighbour)

    return False


def print_all_paths(graph, x, y, visited):
    if x == y:
        path = "->".join([str(node) for node in visited]) + "->" + str(y)
        print("Reached Destination node via {}".format(path))
    visited.append(x)
    neighbours = graph.get(x, [])
    for neighbour in neighbours:
        if neighbour not in visited:
            print_all_paths(graph, neighbour, y, visited)
    visited.pop()


if __name__=="__main__":
    graph = get_graph()
    print(has_path(graph, 0, 6))
    print(print_all_paths(graph, 0, 6, []))