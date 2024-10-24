class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.value, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')

def find_minimum(root):
    while root.left is not None:
        root = root.left
    return root

def delete_node(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_minimum(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)

    return root

def main():
    root = None
    while True:
        value = input("Enter a value to insert into the tree : ")
        if value.lower() == 'q':
            break
        root = insert_node(root, int(value))
    
    print("In-order traversal of the binary tree:")
    in_order_traversal(root)
    print()

    print("Pre-order traversal of the binary tree:")
    pre_order_traversal(root)
    print()

    print("Post-order traversal of the binary tree:")
    post_order_traversal(root)
    print()
# q is use for quit.
    while True:
        value = input("Enter a value to delete from the tree : ")
        if value.lower() == 'q':
            break
        root = delete_node(root, int(value))
        print("In-order traversal after deletion:")
        in_order_traversal(root)
        print()

if __name__ == "__main__":
    main()


