'''
把二叉树打印成多行
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def createBinaryTree(self, root, node):
        if root is None:
            return node
        if root.val > node.val:
            root.left = self.createBinaryTree(root.left, node)
        else:
            root.right = self.createBinaryTree(root.right, node)
        return root

# def pre_order_print(node):
#     # self -- left -- right
#     print(node.val, end=' ')
#     if node.left:
#         pre_order_print(node.left)
#     if node.right:
#         pre_order_print(node.right)

# class Solution1:
#     def Print(self, pRoot):
#         levelList = []
#         if pRoot:
#             levelList.append(pRoot)
#         while len(levelList)!=0:
#             pRoot = levelList.pop(0)
#             print(pRoot.val)
#             levelList.append(pRoot.left)
#             levelList.append(pRoot.right)
#         return

class Solution:
    def Print(self, pRoot):
        if pRoot == None:
            return []
        nodes, res = [pRoot], []
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append((node.right))
            res.append(curStack)
            nodes = nextStack
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(8)
    bt = BinaryTree()
    for i in [6,10,5,7,9,11]:
        bt.createBinaryTree(root,TreeNode(i))
    a = s.Print(root)
    # pre_order_print(root)
    print('\n')
    print(root.right.right.val)
    print(a)