def Add_edge(di, edge):
    u, v = edge
    if u not in di:
        di[u] = []
    if v not in di:
        di[v] = []
    di[u].append(v)
    di[v].append(u)

def Add_node(di, ver):
    if ver not in di:
        di[ver] = []

def display(di):
    for node, edges in di.items():
        print(f"{node}: {edges}")

di = {}

for _ in range(int(input())):
    li = input().split()
    if li[0] == "AddNode":
        Add_node(di, int(li[1]))
    elif li[0] == "AddEdge":
        Add_edge(di, [int(li[1]), int(li[2])])

display(di)
