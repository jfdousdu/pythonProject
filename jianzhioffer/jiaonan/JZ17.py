'''
树的子结构
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        result = False
        if pRoot1.val == pRoot1.val:
            result = self.isSubTree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubTree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right)

#先序遍历树A中的每个节点a，判断树中A以a为根节点的子树是否包含树B


if __name__ == '__main__':
    # 暴力建树
    pRoot1 = TreeNode(1)
    pRoot1.left = TreeNode(2)
    pRoot1.right = TreeNode(3)
    pRoot1.left.left = TreeNode(4)
    pRoot1.left.right = TreeNode(5)

    pRoot2 = TreeNode(2)
    pRoot2.left = TreeNode(1)
    pRoot2.right = TreeNode(5)

    s = Solution()
    a = s.HasSubtree(pRoot1, pRoot2)
    print(a)

