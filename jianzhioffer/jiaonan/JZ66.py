'''
机器人的运动范围
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
#这个题目没有什么合适的思路呢！！！！

#广度优先搜索
# def digitsum(n):
#     ans = 0
#     while n:
#         ans += n%10
#         n //= 10
#     return ans
#
# class Solution:
#     def movingCount(self, threshold, rows, cols):
#         from queue import Queue
#         q = Queue()
#         q.put((0,0))
#         s = set()
#         while not q.empty():
#             x, y = q.get()
#             if (x,y) not in s and 0<=x<rows and 0<=y<cols and digitsum(x) + digitsum(y) <= threshold:
#                 s.add((x, y))
#                 for a, b in [(x+1, y),(x, y+1)]:
#                     q.put((a,b))
#         return len(s)

# #递推
def digitsum(n):
    ans = 0
    while n:
        ans = ans + n % 10
        n = n // 10
    return ans

class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold <= 0:
            return 0
        vis = set([(0,0)])
        for i in range(rows):
            for j in range(cols):
                if ((i-1,j) in vis or (i, j-1) in vis) and digitsum(i)+digitsum(j) <= threshold:
                    vis.add((i, j))
        return len(vis)

if __name__ == '__main__':
    s = Solution()
    threshold = 5
    rows = 10
    cols = 10
    a = s.movingCount(threshold, rows, cols)
    print(a)