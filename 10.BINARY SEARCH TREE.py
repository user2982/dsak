class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Bst:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = node(data)
        
        if self.root is None:
            self.root = newnode
            return
        
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = newnode
                    break 
                else:
                    temp = temp.left 
            elif data > temp.data:
                if temp.right is None:
                    temp.right = newnode
                    break
                else:
                    temp = temp.right
            else:
                break  

    def display(self, node):
        if node:
            self.display(node.left)
            print(node.data, end=" ") 
            self.display(node.right)


tree = Bst()

n = int(input())

for i in range(n):
    s = int(input())
    tree.insert(s)
tree.display(tree.root)
