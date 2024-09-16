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

adj_list = {
    'a': ['b'],
    'b': ['c', 'd'],
    'c': ['f'],
    'd': [],
    'f': ['d']
}


def process_dependencies(edge, adj_list, visited, result):
    for dep in adj_list.get(edge, []):
        if dep not in visited:
            process_dependencies(dep, adj_list, visited, result)
    visited.add(edge)
    result.append(edge)

def main(adj_list):
    result = []
    visited = set()
    for node in adj_list.keys():
        if node not in visited:
            process_dependencies(node, adj_list, visited, result)
            result.append(node)
    print(result)

if __name__=="__main__":
    main(adj_list)