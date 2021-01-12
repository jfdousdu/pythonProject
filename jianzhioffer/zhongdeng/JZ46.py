'''
孩子们的游戏
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。
然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,
并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....
这样下去....直到剩下最后一个小朋友,可以不用表演,
并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
如果没有小朋友，请返回-1
'''
#约瑟夫问题

# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         if n == 0 or m == 0:
#             return -1
#         f = 0
#         for i in range (2, n+1): #此处不明白
#             f = (m + f)% i
#         return f

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return  -1
        if n == 1:
            return 0
        index = 0
        for i in range(2, n+1):
            currentIndex = (index+m)%i
            index = currentIndex
        return index

# class Solution: #python2.X
#     def LastRemaining_Solution(self, n, m):
#         if not m or not n:
#             return -1
#         res = range(n)
#         print(res)
#         i = 0
#         while len(res)>1:
#             i = (m+i-1)%len(res)
#             res.pop(i)
#         return res[0]

#
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         if n == 0:
#             return -1
#         if n == 1:
#             return 0
#         head = Node(0)
#         cur = head
#         for i in range(1, n):
#             cur.next = Node(i)
#             cur = cur.next
#         cur.next = head
#         p = cur
#         while p.next != p:
#             count = 0
#             while count < m - 1:
#                 p = p.next
#                 count += 1
#             p.next = p.next.next
#         return p.val

if __name__ == '__main__':
    s = Solution()
    n = 5
    m = 3
    a = s.LastRemaining_Solution(n, m)

    print(a)
