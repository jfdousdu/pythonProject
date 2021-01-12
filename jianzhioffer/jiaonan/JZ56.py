'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，
请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
‘’‘
#wrong错误原因把它当成数组了其实是列表
# class Solution:
#     def deleteDuplication(self, pHead):
#         deleteDuplicationList = []
#         while pHead:
#             if pHead.val not in deleteDuplicationList:
#                 deleteDuplicationList.append(pHead.val)
#             else:
#                 deleteDuplicationList.pop(-1)
#             pHead = pHead.next
#         return deleteDuplicationList

#如何设置一个循环将链表进行相关的转换，这是最重要的
#好像我有思路但是写不出来
# class Solution:
#     def deleteDuplication(self, pHead):
#         first = ListNode(-1)
#         first.next = pHead
#         last = first
#         while pHead and pHead.next:
#             if pHead.val == pHead.next.val:
#                 val = pHead.val
#                 while pHead and val == pHead.val:
#                     pHead = pHead.next
#                 last.next = pHead
#             else:
#                 last = pHead
#                 pHead = pHead.next
#         return first.next

class Solution:
    def deleteDuplication(self, pHead):
        dummy = ListNode(-1)
        dummy.next = pHead
        pre = dummy
        cur = pHead
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next
        return  dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    s = Solution()
    a = s.deleteDuplication(node1)
    print(a.val)



