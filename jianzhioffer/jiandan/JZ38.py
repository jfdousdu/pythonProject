'''
二叉树的深度
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self,x):
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
        return root #return root在此处的定义好像有特殊含义哦

class Solution:
    def TreeDepth(self,pRoot):
        if pRoot is None:
            return 0
        else:
           n = max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
           return n

root = TreeNode(5)
tree = BinaryTree()

for i in [3,7,8,9]:
    tree.insert(root,TreeNode(i))

s = Solution()
print(s.TreeDepth(root))
