'''
合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
#引入“伪头节点”
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        cur = dum = ListNode(0)  #此处巧妙的把头节点使用了两次
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next, pHead1 = pHead1, pHead1.next
            else:
                cur.next, pHead2 = pHead2, pHead2.next
            cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2
        #Python 三元表达式写法
        # A if x else B ，代表当 x=Truex = Truex=True 时执行 AAA ，否则执行 BBB
        return dum.next

if __name__ == '__main__':
    pHead1 = ListNode(1)
    pHead1.next = ListNode(3)
    pHead1.next.next = ListNode(5)

    pHead2 = ListNode(2)
    pHead2.next = ListNode(4)
    pHead2.next.next = ListNode(6)

    s = Solution()
    a = s.Merge(pHead1,pHead2)
    while a != None:
        print(a.val)
        a = a.next
