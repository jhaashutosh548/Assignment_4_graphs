from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def count_trees(self):
        visited = {v: False for v in self.graph}
        count = 0
        for v in self.graph:
            if not visited[v]:
                self.dfs(v, visited)
                count += 1
        return count


forest = Graph()
forest.add_edge(1, 2)
forest.add_edge(2, 3)
forest.add_edge(4, 5)

tree_count = forest.count_trees()
print("Number of trees in the forest:", tree_count)