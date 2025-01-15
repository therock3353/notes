'''
    Topological sort:
        can only be done on DIRECTED ACYCLIC Graphs

        a  -----> b  ----->g
                  |
                  v
        d <------ c ------->e

        a: []
        b: [a]
        c: [b, f]
        d: [c]
        e: [b]
        f: [e]
        g: [b]

    def process_dependencies(edge, adj_list, visited, result):
        for dep in adj_list.get(edge, []):
            self.process_dependencies(dep, adj_list, visited)
        visited.add(edge)
        result.append(edge)

    def main():
        result = []
        visited = set()
        for node in adj_list.keys():
            if node not in visited:
                process_dependencies(node)
            result.append(node)

'''

# adj_list = {
#     'a': ['b'],
#     'b': ['c', 'd'],
#     'c': ['f'],
#     'd': [],
#     'f': ['d']
# }
#
#
# def process_dependencies(edge, adj_list, visited, result):
#     for dep in adj_list.get(edge, []):
#         if dep not in visited:
#             process_dependencies(dep, adj_list, visited, result)
#     visited.add(edge)
#     result.append(edge)
#
# def main(adj_list):
#     result = []
#     visited = set()
#     for node in adj_list.keys():
#         if node not in visited:
#             process_dependencies(node, adj_list, visited, result)
#             result.append(node)
#     print(result)

'''
    In Topological Sort, you have to take care of cycle use case. If there is a cycle,
    then you cannot proceed because then it is not a DAG. 
    
    There are two use cases to handle:
        visited => when a node is processed completely, ie all neighbours
            are visited and they come back. In post-processing, we mark the node 
            as visited and add it to queue []. 
            Once node is visited, we don't want to visit it again.
            
        cycle = set() => is used to track if there is a cycle or not.
            A ----- > C
            |         ^  
            V         |
            B --------   
            
            When you start from A, need to keep track of A but A is still not visited.
            A -> B
                 B -> C (C is now processed)
            A -> C
                But is C was already visited so is this a cycle? but no there is no cycle.
                To handle this case we have another set() cycle.
                Once B visits C, it will add it to cycle-set but once the node is processed,
                it will remove it from cycle-set.
                It is a cycle only when during the processing of the node, the same node is visited.
'''

dag = {
    1: [2],
    2: [],
    3: [1],
    4: [2, 3, 5],
    5: [1],
    6: [2, 5],
}

class TopologicalSort(object):
    def dfs(self, node, graph, visited, cycle, result):
        if node in visited:
            return False
        if node in cycle:
            return True
        cycle.add(node)
        for neighbour in graph.get(node, []):
            res = self.dfs(neighbour, graph, visited, cycle, result)
            if res is True:
                return res
        cycle.remove(node)
        visited.add(node)
        result.append(node)
        return False

    def srt(self, graph):
        if not graph:
            return []
        visited = set()
        cycle = set()
        result = []
        for node in graph.keys():
            res = self.dfs(node, graph, visited, cycle, result)
            if res is True:
                return []
        return result

print(TopologicalSort().srt(graph=dag))
