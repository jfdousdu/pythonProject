'''
序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！
表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，
然后通过自己的函数来解析回这个二叉树
'''
#没有理解意思

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def createBinaryTree(root, node):
    if root is None:
        return node
    if root.val > node.val:
        root.left = createBinaryTree(root.left, node)
    if root.val < node.val:
        root.right = createBinaryTree(root.right, node)
    return root

class Solution:
    # 序列化
    def Serialize(self, root):
        if root is None:
            return "[]"
        serializeList = []
        tmpList = []
        tmpList.append(root)
        while(len(tmpList)!=0):
            tmp = tmpList.pop(0)
            if tmp:
                serializeList.append(str(tmp.val))
                tmpList.append(tmp.left)
                tmpList.append(tmp.right)
            else:
                serializeList.append('Null')
        return '['+','.join(serializeList)+']'

    #反序列化
    def Deserialize(self, s):
        if s == "[]":
            return
        vals, i  = s.split(','),1
        root = TreeNode(int(vals[0]))
        queue = []
        queue.append(root)
        while i< len(vals) and queue:
            node = queue.pop(0)
            if vals[i]!= 'Null':
                node.left = TreeNode(vals[i])
                queue.append(node.left)
            i = i+1
            if vals[i] != 'Null':
                node.right = TreeNode(vals[i])
                queue.append(node.right)
            i = i+1
        print(root.right.right.val)
        return root

if __name__ == '__main__':
    # s = Solution()
    # root = TreeNode(1)
    # for i in [2,3,4,5]:
    #     createBinaryTree(root, TreeNode(i))
    # a = s.Serialize(root)
    # print(a)
    sol = Solution()
    s = '2,1,3,Null,Null,4,5'
    sol.Deserialize(s)
