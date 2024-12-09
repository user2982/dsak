class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_after(self, x, y):
        temp = self.head
        while temp:
            if temp.data == y:
                new_node = Node(x)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next

    def display(self):
        if self.head is None:
            print("The list is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def delete_tail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next and temp.next.next:
            temp = temp.next
        temp.next = None

    def delete_node(self, x):
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == x:
                temp.next = temp.next.next
                return
            temp = temp.next

obj = SLL()
n = int(input())
for i in range(n):
    s = list(map(int, input().split()))
    if s[0] == 1:
        obj.insert_at_beg(s[1])
    elif s[0] == 2:
        obj.insert_at_end(s[1])
    elif s[0] == 3:
        obj.insert_after(s[1], s[2])
    elif s[0] == 4:
        obj.display()
    elif s[0] == 5:
        obj.delete_tail()
    elif s[0] == 6:
        obj.delete_node(s[1])
