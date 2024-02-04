class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def in_or(root):
    if root:
        in_or(root.left)
        print(root.val, end=",")
        in_or(root.right)

def pre_or(root):
    if root:
        print(root.val, end=",")
        pre_or(root.left)
        pre_or(root.right)

def post_or(root):
    if root:
        post_or(root.left)
        post_or(root.right)
        print(root.val, end=",")

if __name__ == "__main__":
    keys = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44, 66, 90]

    root = None
    for key in keys:
        root = insert(root, key)

    print("In-order:")
    in_or(root)

    print("\nPre-order:")
    pre_or(root)

    print("\nPost-order:")
    post_or(root)
