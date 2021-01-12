'''
二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
我们利用中序遍历进行求解
'''
'''
双向链表：每个节点保存next结合prev两个属性
'''
///
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None

        root = TreeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order + 1:], tin[order + 1:])
                return root

class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return
        if pRootOfTree.left:
            pRootOfTree.left = self.Convert(pRootOfTree.left)
        print(pRootOfTree.val)
        if pRootOfTree.right:
            pRootOfTree.left = self.Convert(pRootOfTree.right)