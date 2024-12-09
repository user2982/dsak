class queue:
    def __init__(self):
        self.arr = []

    def enrear(self, val):
        return self.arr.append(val)

    def derear(self):
        return self.arr.pop()

    def enfront(self, val):
        return self.arr.insert(0, val)

    def defront(self):
        return self.arr.pop(0)

    def rearpeek(self):
        return self.arr[-1]

    def frontpeek(self):
        return self.arr[0]

    def display(self):
        print(len(self.arr))

res = queue()
n = int(input())
for i in range(n):
    oper = input().split()
    if len(oper) >= 2:
        op = oper[0]
        val = oper[1]
    else:
        op = oper[0]

    if op == "append":
        res.enrear(val)
    elif op == "appendleft":
        res.enfront(val)
    elif op == "pop":
        r = res.derear()
        print(r)
    elif op == "popleft":
        r = res.defront()
    elif op == "peek":
        r = res.rearpeek()
        print(r)
    elif op == "peekleft":
        r = res.frontpeek()
        print(r)
    elif op == "size":
        res.display()
