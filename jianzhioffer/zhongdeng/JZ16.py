'''
合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

、、class List:
    def createList(self, pHead, node):
        if pHead is None:
            return node
        if pHead.next:
            pHead.next = self.createList(pHead.next, node)
        if pHead.next == None:
            pHead.next = node
        return pHead

class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
