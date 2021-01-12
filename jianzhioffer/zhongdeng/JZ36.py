'''
两个链表的第一个公共节点：
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
'''

#此处验证并不明确
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createList(pHead, node):
    if pHead == None:
        return node
    while pHead.next!= None:
        pHead = pHead.next
    pHead.next = node
#
# class Solution:
#     def FindFirstCommonNode(self, pHead1, pHead2):
#         while pHead1:
#             pHead3 = pHead2
#             while pHead3:
#                 if pHead1.val == pHead3.val:
#                     return pHead1.val
#                 else:
#                     pHead3 = pHead3.next
#             pHead1 = pHead1.next
#         return

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        node1, node2 = pHead1, pHead2
        print(node2.val)
        while node1!=node2:
            if node1 == None:
               node1 = pHead2
            else:
               node1 = node1.next
            if node2 == None:
               node2 = pHead1
               print(node2.val, "+")
            else:
               node2 = node2.next
               print(node2.val,"++")
        return node2.val

if __name__ == '__main__':
    s = Solution()
    pHead1 = ListNode(2)
    pHead2 = ListNode(6)
    for i in [3,14,5]:
        createList(pHead1, ListNode(i))
    for j in [9,4,3,1,9]:
        createList(pHead2, ListNode(j))

    a = s.FindFirstCommonNode(pHead1, pHead2)
    print(a,pHead1.next.next.val,'+')

