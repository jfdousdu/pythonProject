'''
二叉树中为某一值的路径
输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

#思路：每个根节点到叶子节点的和为确定整数则输出该路径即可
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def FindPath(self, root, expectNumber):
#         expectList = []
#         tmpList = []
#         def recur(root, expectNumber):
#             if not root:
#                 return
#             tmpList.append(root.val)
#             expectNumber = expectNumber - root.val
#             if expectNumber == 0 and root.left == None and root.right == None:
#                 expectList.append(list(tmpList))
#             recur(root.left, expectNumber)
#             recur(root.right, expectNumber)
#             tmpList.pop() #题目的关键
#
#         recur(root, expectNumber)
#         return expectList

class Solution:
    def FindPath(self, root, expectNumber):
        self.res = []
        if not root:
            return []
        self.subPath(root, [], expectNumber)
        return self.res

    def subPath(self, root, path, number):
        if not root.left and not root.right:
            if number == root.val:
                self.res.append(path+[root.val]) #注意此处
        if root.left:
            self.subPath(root.left, path+[root.val], number-root.val)
        if root.right:
            self.subPath(root.right, path + [root.val], number-root.val)

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    expectNumber = 22

    s = Solution()
    a = s.FindPath(root,expectNumber)
    print(a)