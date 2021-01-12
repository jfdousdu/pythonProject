'''
对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isSymmetrical(self, pRoot):
#         if not pRoot:
#             return True
#         def dfs(left, right):
#             if not (left or right):
#                 return True
#             if not (left and right):
#                 return False
#             if left.val != right.val:
#                 return False
#             return dfs(left.left, right.right) and dfs(left.right, right.left)
#         return dfs(pRoot.left, pRoot.right)
#
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True
        return self.isSymmetricTree(pRoot.left, pRoot.right)

    def isSymmetricTree(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricTree(left.left, right.right) and self.isSymmetricTree(left.right, right.left)

node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(6)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(7)
node7 = TreeNode(6)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s = Solution()
a = s.isSymmetrical(node1)
print(a)

