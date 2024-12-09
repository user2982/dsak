def adjacencyList(ver, edge):
    li = [i + 1 for i in range(ver)]
    di = {}
    for i in li:
        di[i] = []
    for i, j in edge:
        di[i].append(j)
        di[j].append(i)
    return di

def bfs(adjLis):
    st = int(input())
    que = [st]
    vis = []
    while que:
        x = que.pop(0)
        vis.append(x)
        for i in adjLis[x]:
            if i not in que and i not in vis:
                que.append(i)
    print(*vis)

n = int(input())
li = []
for i in range(n - 1):
    li.append(list(map(int, input().split())))
aLi = adjacencyList(n, li)
bfs(aLi)
