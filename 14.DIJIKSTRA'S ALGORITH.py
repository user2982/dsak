class graph:
    def __init__(self, val):
        self.ver = val
        self.graph = [[0 for i in range(val)] for i in range(val)]
    
    def addedge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w
    
    def mindistance(self, d, b):
        a = float('inf')
        a_index = -1
        for i in range(self.ver):
            if d[i] < a and not b[i]:
                a = d[i]
                a_index = i
        return a_index
    
    def dijkstra(self, src):
        d = [float('inf')] * self.ver
        d[src] = 0
        b = [False] * self.ver
        for i in range(self.ver):
            u = self.mindistance(d, b)
            b[u] = True
            for v in range(self.ver):
                if self.graph[u][v] > 0 and not b[v] and d[u] + self.graph[u][v] < d[v]:
                    d[v] = d[u] + self.graph[u][v]
        return d

n = int(input())
G = graph(n)
m = int(input())
for i in range(m):
    u, v, w = map(int, input().split())
    G.addedge(u, v, w)
src = int(input())
res = G.dijkstra(src)
for i in range(len(res)):
    print(res[i])
