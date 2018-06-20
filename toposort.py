class Graph:
    def __init__(self, v):
        self.adj = [set() for _ in range(v)]
        
    
    def addEdge(self, v1, v2, w):
        self.adj[v1].add((v2, w))
    
    def topoSort(self, v, visited, stack):
        if visited[v] == 1:
            return
        if visited[v] == 2:
            return
        
        visited[v] = 1
        for node in self.adj[v]:
            self.topoSort(node[0], visited, stack)

        visited[v] = 2
        stack.append(v)
    
    def shortestDistance(self, v):
        visited = [0] * 5
        stack = []
        self.topoSort(v, visited, stack)
        
        dist = [float("inf")] * len(self.adj)
        dist[v] = 0
        
        while stack:
            i = stack.pop()
            for node in self.adj[i]:
                print (v, dist[v] + node[1])
                if dist[node[0]] > dist[i] + node[1]:
                    dist[node[0]] = dist[i] + node[1]
        
        # Outputs shortest distance from vertex V to child nodes
        print(dist)

g = Graph(5)
g.addEdge(0, 2, 2)
g.addEdge(0, 3, 3)
g.addEdge(0, 4, 5)
g.addEdge(2, 3, 4)
g.addEdge(2, 1, 10)
g.addEdge(1, 3, 2)
g.addEdge(4, 1, 1)

g.shortestDistance(0)
