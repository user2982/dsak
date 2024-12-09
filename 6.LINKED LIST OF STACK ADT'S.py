class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, x):
        newnode = node(x)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.isEmpty():
            return "True"
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

obj = stack()
n = int(input())
for _ in range(n):
    oper = input().split()
    if oper[0] == "push":
        obj.push(int(oper[1]))
    elif oper[0] == "pop":
        print(obj.pop())
    elif oper[0] == "peek":
        print(obj.peek())
    elif oper[0] == "isEmpty":
        print(obj.isEmpty())
    elif oper[0] == "size":
        print(obj.size())
