'''
链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个结点。
1,{1,2,3,4,5}
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def createListNode(phead, node):
    if phead == None:
        return phead

    while phead.next != None:
        phead = phead.next

    phead.next = node
    print(phead.val)

class Solution:

    def FindKthToTail(self, head, k):
        if head == None:
            return
        list = []
        number = 0

        while head != None:
            list.append(head)
            head = head.next
            number += 1

        if k > number or k <= 0:
            return

        return list[number-k]

if __name__ == '__main__':
    s = Solution()
    phead = ListNode()
    for i in [ ]:
        createListNode(phead,ListNode(i))

    a = s.FindKthToTail(phead, 100)
    print(a.val)