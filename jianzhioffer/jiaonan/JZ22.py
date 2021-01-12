'''
从上往下打印二叉树
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        # left-- right--self
        if root == None:
            return []
        q = []
        res = []
        q.append(root)
        while q:
            current = q.pop(0)
            res.append(current.val)
            if current.left != None:
                q.append(current.left)
            if current.right != None:
                q.append(current.right)
        return res


# class Solution:
#     def PrintFromTopToBottom(self, root):
#         if not root:
#             return []
#         stack = [root]
#         res = []
#         while stack:
#             temp = stack
#             stack = []
#             for node in temp:
#                 res.append(node.val)
#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
#         return res

# def PrintFromTopToBottom(self, root):
#     # left-- right--self
#     if root == None:
#         return []
#     q = []
#     res = []
#     q.append(root)
#     while q:
#         current = q.pop(0)
#         res.append(current.val)
#         if current.left!=None:
#             q.append(current.left)
#         if current.right!=None:
#             q.append(current.right)
#     return res

if __name__ == '__main__':
    s = Solution()
    Node = TreeNode(5)
    Node.left = TreeNode(4)
    Node.right = TreeNode('#')
    Node.left.left = TreeNode(3)
    Node.left.right = TreeNode(None)
    Node.left.left.left = TreeNode(2)
    Node.left.left.right = TreeNode(None)
    Node.left.left.left.left = TreeNode(1)
    Node.left.left.left.right = TreeNode(None)

    root = Node
    a = s.PrintFromTopToBottom(root)

    print(a,Node.left.val)


