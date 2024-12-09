class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = node(data)
        if self.root is None:
            self.root = newnode
            return
        
        queue = [self.root]
        
        while queue:
            temp = queue.pop(0) 
            
            if temp.left is None:
                temp.left = newnode
                break
            else:
                queue.append(temp.left) 
            
            if temp.right is None:
                temp.right = newnode
                break
            else:
                queue.append(temp.right) 

    def display(self):
        if not self.root:
            print("The tree is empty.")
            return

        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        print() 
tree = binarytree()
m = int(input())
nums = list(map(int, input().split()))
for i in range(m):
    tree.insert(nums[i])

tree.display()
