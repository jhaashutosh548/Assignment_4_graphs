
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, recursion_stack):
        visited[v] = True
        recursion_stack.add(v)

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(v)
        return False

    def is_cyclic(self):
        visited = {v: False for v in self.graph}
        recursion_stack = set()

        for v in self.graph:
            if not visited[v]:
                if self.is_cyclic_util(v, visited, recursion_stack):
                    return True

        return False


graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

if graph.is_cyclic():
    print("Cycle exists in the graph")
else:
    print("No cycle found in the graph")