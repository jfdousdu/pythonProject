'''
反转链表
输入一个链表，反转链表后，输出新链表的表头。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def crateListNode(self, pHead, node):
        if pHead is None:
            return node
        if pHead.next:
            pHead.next = self.crateListNode(pHead.next,node)
        if pHead.next == None:
            pHead.next = node
        return pHead

class Solution:
    def ReverseList(self, pHead):
        if pHead != None:
            q = None
            while pHead:
                temp = pHead.next
                pHead.next = q
                q = pHead
                pHead = temp
            return q

def prlist(node):
    while node.next:
        print(node.val)
        node = node.next
    return


pHead = ListNode(5)
list = List()

for i in [5,3,7,8,9]:
    list.crateListNode(pHead,ListNode(i))

s = Solution()
a = s.ReverseList(pHead)
print(a.val)
print(prlist(a))