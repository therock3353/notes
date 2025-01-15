'''
    This only works for un-directed graphs.
    Using BFS.

    A  ---- B ----  C
    |               |
      ------D ------

    There is a cycle. You can reach C by both paths A->B or A->D.
    If there is a cycle then you will hit the node twice. You have to look for this specific condition.
    goto node A
        node is not visited
        mark visited
        if neighbour (B, D) not in visited:
            Q = [B, D]

    goto node B
        node is not visited
        mark visited
        neighbour A already in visited:
            continue
        if neighbour (C) not in visited:
            Q = [D, C]

    goto node D
        node is not visited
        mark visited
        neighbour A already in visited:
            continue
        if neighbour (C) not in visited:
            Q = [C, C]          <======== There are 2 C's in the queue because you can reach C via 2 different paths,
                                            because of the cycle.
    goto node C
        node is not visited
        mark visited
        neighbour B, D already in visited:
            continue
        Q = [C]

    goto node C
        node is already in visited
        There is a cycle
'''
graph = {
    'a': ['b', 'd'],
    'b': ['c', 'd'],
    'c': [],
    'd': ['c']
}

graph_without_cycle = {
    'a': ['b', 'd'],
    'b': ['a'],
    'c': ['d'],
    'd': ['c']
}

from queue import Queue
class UndirectedGraphCycle(object):

    def isCycle(self, graph):
        queue = Queue()
        visited = set()
        queue.put(list(graph.keys())[0])
        while not queue.empty():
            node = queue.get()
            if node in visited:
                return True
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    queue.put(neighbour)

        return False


print(UndirectedGraphCycle().isCycle(graph))