'''
二叉搜索树的后学遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def createBinaryTree(self, root, node):
#         if root is None:
#             return node
#         if root.val > node.val:
#             root.left = self.createBinaryTree(root.left, node)
#         if root.val < node.val:
#             root.right = self.createBinaryTree(root.right, node)
#         return root

# #自己写的方法本地正确，可是没有root值的传递，导致在平台上测试不行
# class Solution:
#     def __init__(self):
#         self.LRD = []
#
#     def printLRD(self, root):
#         if root.left:
#             self.printLRD(root.left)
#         if root.right:
#             self.printLRD(root.right)
#         self.LRD.append(root.val)
#         print(self.LRD)
#         return self.LRD
#
#     def VerifySequenceOfBST(self, sequence):
#         if sequence == self.printLRD(root):
#             return True
#         else:
#             return False
#
# if __name__ == '__main__':
#     s = Solution()
#     b = BinaryTree()
#     root = TreeNode(2)
#     for i in [4,1,3,5]:
#         b.createBinaryTree(root, TreeNode(i))
#     print(root.right.val)
#     # a= s.printLRD(root)
#     # print(a)
#
#     t = s.VerifySequenceOfBST([1,3,5,4,2])
#     print(t)

#递归法
#这种方法是依据树的性质进行判断 左子树（左、右、根）、右子树、根节点。
class Solution:
    def VerifySequenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        index = 0
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                index = i
                break
        for j in range(i,len(sequence)):
            if sequence[j] < sequence[-1]:
                return False
        left = True
        right = True
        if len(sequence[:index]) > 0:
            left = self.VerifySequenceOfBST(sequence[:index])
        if len(sequence[index:-1])> 0:
            right = self.VerifySequenceOfBST(sequence[index:-1])
        return left and right

if __name__ == '__main__':
    s = Solution()
    t = s.VerifySequenceOfBST([1,3,5,4,8])
    print(t)