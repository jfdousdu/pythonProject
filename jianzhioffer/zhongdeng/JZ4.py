'''
重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
'''
先序遍历和中序遍历的关系，先序遍历的第一个值是根节点的值。在中序遍历中，根节点左边的值是左子树，右边的值是右子树上的值。
'''
#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pre_order_tree(node):
    print(node.val," ")
    if node.left:
        pre_order_tree(node.left)
    if node.right:
        pre_order_tree(node.right)

def build_pre_in_order(pre_order,in_order):
    if not pre_order:
        return None

    root = TreeNode(pre_order[0])
    index = in_order.index(root.val)
    root.left = build_pre_in_order(pre_order[1:index+1],in_order[0:index])
    root.right = build_pre_in_order(pre_order[index+1:],in_order[index+1:])
    print(root.val)#为什么不能读取
    return root

if __name__ == '__main__':

    preorder = [1,2,3,4,5,6,7]
    inorder = [3,2,4,1,6,5,7]
    root = build_pre_in_order(preorder,inorder)
    print(" ")
    print(root.val," ")
    print(" ")
    pre_order_tree(root)

# class Solution:
#
#     def reConstructBinaryTree(self,pre_order, in_order):
#         if not pre_order:
#             return None
#
#         root = TreeNode(pre_order[0])
#         index = in_order.index(root.val)
#         root.left = self.reConstructBinaryTree(pre_order[1:index + 1], in_order[0:index])
#         root.right = self.reConstructBinaryTree(pre_order[index + 1:], in_order[index + 1:])
#         return root
