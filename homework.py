class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root is not None
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def inorder_traversal(root, result):
    if root is not None:
        inorder_traversal(root.left, result)
        result.append(root.key)
        inorder_traversal(root.right, result)

def main():
    root = None
    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Inorder")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            key = int(input("Enter element: "))
            root = insert(root, key)
        elif choice == '2':
            key = int(input("Enter element: "))
            if search(root, key):
                print("Exists")
            else:
                print("Does not exist")
        elif choice == '3':
            result = []
            inorder_traversal(root, result)
            print("Inorder:", result)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
