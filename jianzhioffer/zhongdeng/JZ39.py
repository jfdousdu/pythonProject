'''
平衡二叉树
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree:
    def createTree(self, Root):
        if Root == None:
            return Root


class Solution:

    def IsBalanced_Solution(self, pRoot):
        deepLeft = 0
        deepRight = 0
        deep = 0
        self.flag = True

        if pRoot == None:
            return 0

        if pRoot.left:
            deepLeft = self.IsBalanced_Solution(pRoot.left) + 1
        if  pRoot.left:
            deepRight = self.IsBalanced_Solution(pRoot.right) +1

        deep = max(deepLeft,deepRight)

        if abs(deepLeft-deepRight) <= 1:
            return deep
        else:
            self.flag = False

        return self.flag
