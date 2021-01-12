'''
二叉搜索树的第k个结点
给定一棵二叉搜索树，请找出其中的第k小的结点。
'''
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root, node):
        if root is None:
            return node
        if root.value > node.value:
            root.left = self.insert(root.left, node)
        if root.value < node.value:
            root.right = self.insert(root.right, node)
        return root
#
# class Solution:
#    Kth=[]
#    def KthNode(self, pRoot, k):
#        if k > 0 and pRoot is not None:
#            if pRoot.left:
#                self.KthNode(pRoot.left, k)
#            self.Kth.append(pRoot.value)
#            if len(self.Kth) >= k:
#                d = self.Kth[k - 1]
#                return d  # 存在问题
#            if pRoot.right:
#               self.KthNode(pRoot.right, k)


class Solution:
   def __init__(self): #关键之处，不然会在一定程度上进行报错
        self.Kth = []
   def KthNode(self, pRoot, k):
       ans=None
       if k > 0 and pRoot is not None:
           if pRoot.left:
               ans=self.KthNode(pRoot.left, k)
           self.Kth.append(pRoot.value)
           if ans is not None:
               return ans
           if len(self.Kth) == k:
               d = self.Kth[k - 1]
               return d  # 存在问题
           if pRoot.right:
               ans=self.KthNode(pRoot.right, k)
       return ans

# class Solution:
#    def __init__(self):
#         self.Kth = []
#    def KthNode(self, pRoot, k):
#        if k > 0 and pRoot is not None:
#            if pRoot.left:
#                self.KthNode(pRoot.left, k)
#            self.Kth.append(pRoot) #pRoot.value 验证的值是正确的
#            if pRoot.right:
#                self.KthNode(pRoot.right, k)
#            if len(self.Kth) >= k:
#                print(1)
#                return self.Kth[k - 1]  # 存在问题,改进的原因是什么
#输出节点，日，找了半天错误，

if __name__ == '__main__':
    root = TreeNode(9)
    btree = BinaryTree()
    for i in [8,6,10,5,7,11]:
        btree.insert(root,TreeNode(i))
    s = Solution()

    a = s.KthNode(root,8)
    print(a)
