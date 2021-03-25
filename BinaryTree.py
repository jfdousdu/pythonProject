class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root, node):
        if root is None:
            return node
        if node.value < root.value:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)

        return root

class Solution:
    def Mirror(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        if root.left != None:
            self.Mirror(root.left)
        if root.right != None:
            self.Mirror(root.right)

def pre_order_print(node):
    # self -- left -- right
    print(node.value, end=' ')
    if node.left:
        pre_order_print(node.left)
    if node.right:
        pre_order_print(node.right)

def mid_order_print(node):
    # mid --self -- right
    if node.left:
        mid_order_print(node.left)
    print(node.value, end = ' ')
    if node.right:
        mid_order_print(node.right)

def after_order_print(node):
    # left-- right--self
    if node.left:
        after_order_print(node.left)
    if node.right:
        after_order_print(node.right)
    print(node.value, end=' ')

def level_order_print(node):
    # left-- right--self
    if node == None:
        return
    q = []
    q.append(node)
    while q:
        current = q.pop(0)
        print(current.value,end=' ')
        if current.left!=None:
            q.append(current.left)
        if current.right!=None:
            q.append(current.right)

if __name__ == '__main__':

    root = Node(8)
    tree = BinaryTree()
    s = Solution()


    for i in [6, 10, 5, 7, 9, 11]:
        tree.insert(root, Node(i))

    level_order_print(root)
    print('\n')
    print('\n')

    mid_order_print(root)
    print('\n')
    pre_order_print(root)
    print('\n')
    after_order_print(root)
    print('\n')
    print('\n')

    print(root.left.left.value)