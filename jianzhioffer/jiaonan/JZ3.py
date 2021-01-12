'''
从尾到头打印链表
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
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
    #利用栈进行求解
    # def printListFromTailToHead1(self, listNode):
    #     stackNode = []
    #     ArrayList = []
    #     if listNode  == None:
    #         return []
    #     while listNode.val != None:
    #         stackNode.append(listNode.val)
    #         listNode = listNode.next
    #     n = len(stackNode)
    #     if n == 0:
    #         return []
    #     if n> 0:
    #         for  i in range(0,n):
    #             ArrayList.append(stackNode[n-i-1])
    #     return ArrayList


    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        p = listNode
        stack = []
        res = []
        while p:
            stack.append(p.val)
            p = p.next
        for i in range(len(stack)-1,-1,-1):
            res.append(stack[i])
        return res

pHead = ListNode(4)
list = List()

for i in [5,7,8]:
    list.crateListNode(pHead,ListNode(i))

s = Solution()
a = s.printListFromTailToHead(pHead)
print(a)