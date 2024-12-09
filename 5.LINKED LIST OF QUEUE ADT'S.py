class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        newnode = node(data)
        if self.is_empty():
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_value = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return dequeued_value

    def front_value(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        return self._size

queue = Queue()
n = int(input()) 
for _ in range(n):
    oper = input().split() 
    if oper[0] == "enqueue":
        queue.enqueue(int(oper[1]))
    elif oper[0] == "dequeue":
        print(queue.dequeue())
    elif oper[0] == "front":
        print(queue.front_value())
    elif oper[0] == "is_empty":
        print(queue.is_empty())
    elif oper[0] == "size":
        print(queue.size())
