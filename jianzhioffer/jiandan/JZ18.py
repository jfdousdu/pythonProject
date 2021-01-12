'''
二叉树的镜像
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root, node):
        if root is None:
            return node
        if root.val > node.val:
            root.left = self.insert(root.left,node)
        else:
            root.right = self.insert(root.right,node)
        return root

class Solution:
    def Mirror(self, root):
       if not root:
           return None
       root.left,root.right = root.right,root.left
       if root.left !=  None:
           self.Mirror(root.left)
       if root.right != None:
           self.Mirror(root.right)

def level_order_print(node):
    # left-- right--self
    if node == None:
        return
    q = []
    q.append(node)
    while q:
        current = q.pop(0) #巧妙的借助列表这一概念进行存储
        print(current.val,end=' ')
        if current.left!=None:
            q.append(current.left)
        if current.right!=None:
            q.append(current.right)

root = TreeNode(5)
tree = BinaryTree()

for i in [2, 11, 7, 3, 9, 8, 4, 6, 1]:
    tree.insert(root,TreeNode(i))
level_order_print(root)
print('\n')

s = Solution()
s.Mirror(root)
level_order_print(root)

