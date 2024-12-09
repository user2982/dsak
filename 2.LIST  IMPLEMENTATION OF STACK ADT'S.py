class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.stack[-1]
    def display(self):
        return self.stack
obj = Stack()
n = int(input("Enter the number of operations: "))

for i in range(n):
    l = list(map(str, input().split()))
    
    if l[0] == "push":
        obj.push(int(l[1]))
    elif l[0] == "pop":
        popped_value = obj.pop()
        if popped_value is not None:
            print(f"Popped value: {popped_value}")
    elif l[0] == "peek":
        val = obj.peek()
        print(val)
