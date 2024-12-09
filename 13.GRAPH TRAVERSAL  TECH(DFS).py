def adjacencyTraversal(ver, edge):
    li = []
    for i in range(ver):
        li.append([0] * ver)
    for x, y in edge:
        li[x][y] = 1
        li[y][x] = 1
    return li

def dfs(Mli, st, n):
    stac = [st]
    vis = []
    while stac:
        ini = stac.pop()
        if ini not in vis:
            vis.append(ini)
        for j in range(n - 1, -1, -1):
            if Mli[ini][j] == 1:
                if j not in vis:
                    stac.append(j)
    print(*vis)

ver, edge = map(int, input().split())
edj = []
for i in range(edge):
    edj.append(list(map(int, input().split())))

adj = adjacencyTraversal(ver, edj)
st = int(input())
dfs(adj, st, ver)
