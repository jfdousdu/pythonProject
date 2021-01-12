'''
链表中环的入口结点
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
#快慢双指针
#做此题的时候没有思路
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# def createList(pHead, node): #生成一个与next相关的链表
#     if pHead is None:
#         return node
#     while pHead.next:
#         pHead = pHead.next
#     pHead.next = node
#     return


# class Solution:  #这是答案极力推荐的
#     def EntryNodeOfLoop(self, pHead):
#         if pHead == None or pHead.next == None or pHead.next.next == None:
#             return None
#         low = pHead.next
#         fast = pHead.next.next
#         while low != fast:
#             if fast.next == None or fast.next.next == None:
#                 return None
#             low = low.next
#             fast = fast.next.next
#         fast = pHead
#         while low != fast:
#             low = low.next
#             fast = fast.next
#         return fast

class Solution: #存在部分判断不完整的缺点
    def EntryNodeOfLoop(self, pHead):
        listValue = []
        while pHead:
            if pHead.val not in listValue:
                listValue.append(pHead.val)
                pHead = pHead.next
            else:
                return pHead

# if __name__ == '__main__':
#     pHead = ListNode(1)
#     for i in [ 2, 9, 3, 4, 3]:
#         createList(pHead,ListNode(i))
#     s = Solution()
#     a = s.EntryNodeOfLoop(pHead)
#     print(a)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)