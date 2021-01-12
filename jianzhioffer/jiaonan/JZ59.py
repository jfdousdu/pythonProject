'''
按之字形顺序打印二叉数
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createdBinaryTree(root, node):
    if root is None:
        return  node
    if root.val > node.val:
        root.left = createdBinaryTree(root.left, node)
    else:
        root.right = createdBinaryTree(root.right, node)
    return root

#应该在层序遍历的基础上添加特定条件，输出符合条件的结果
def levelBinaryTree(root):
    levelList = []
    if root == None:
        return
    levelList.append(root)
    while len(levelList)!= 0:
        tmp = levelList.pop(0)
        print(tmp.val)
        if tmp.left:
            levelList.append(tmp.left)
        if tmp.right:
            levelList.append(tmp.right)

class Solution:
    def Print(self, pRoot):
        levelList = []
        allLevelList = []
        flag = 1  #flag标志判断，若flag为负则表示偶数行。从右往左遍历

        if pRoot == None:
            return []
        levelList.append()
        while len(levelList) != 0:
            tempList = []
            tempLen = len(levelList)
            for i in range(tempLen):
                temp = levelList.pop(0)
                tempList.append(temp.val)
                if temp.left:
                    levelList.append(temp.left)
                if temp.right:
                    levelList.append(temp.right)
            if flag == -1:
                tempList = tempList[:: -1] #所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。所以你看到一个倒序的东东
            allLevelList.append(tempList)
            flag *= -1
        return allLevelList


if __name__ == '__main__':
    root = TreeNode(8)
    for i in [6,10,5,7,9,11]:
        createdBinaryTree(root, TreeNode(i))
    levelBinaryTree(root)
    s = Solution()
    a = s.Print(root)
    print(a)