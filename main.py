class Node:
    def __init__(self,a):
        self.data = a
        self.left = None
        self.right = None


def Inorder(root):
    if root is not None:
        if root.left is not None:
            Inorder(root.left)

        print(root.data)             
        if root.right is not None:
            Inorder(root.right)

def insert(root,x):
    if root == None:
        return Node(x)
    if x < root.data:
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x)    
    return root

def search(root,key):
    if root.data == key:
        return root
    elif key < root.data and root.left is not None:
        return search(root.left,key)
    elif key > root.data and root.right is not None:
        return search(root.right,key)
    else:
        return -1

element = int(input("Enter the number of elements you want: "))  
root = None 

for i in range(1,element+1):
    x = int(input(f"Enter the element {i}: "))
    
    root = insert(root,x)

Inorder(root)
key = int(input("Enter the number you want searched: "))

keyNode = search(root,key)
if keyNode == -1:
    print("Key Doesn't Exist")
else:
    print("Key Exists")