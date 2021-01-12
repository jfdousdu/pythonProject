'''
滑动窗口的最大值
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}，
 {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
 {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
窗口大于数组长度的时候，返回空
'''
#自己的方法：求每次窗口的最大值，时间复杂度O(n*size)。
# class Solution:
#     def maxInWindows(self, num, size):
#         n = len(num)
#         i = 0
#         j = size
#         if j == 0:
#             return []
#         maxListNumber = []
#         for i in range(0, n-size+1):
#             j = i + size
#             maxListNumber.append(max(num[i:j]))
#         return maxListNumber

#如何在每次窗口滑动后，将获取窗口内的元素的最大值将时间复杂度从o(K)降到o(1).

import collections
class Solution:
    def maxInWindows(self, num, size):
        if not num or size==0 or size > len(num):
            return []
        deque = collections.deque()
        for i in range(size): #未形成窗口
            while deque and deque[-1] < num[i]:
                deque.pop()
            deque.append(num[i])
        res = [deque[0]]
        for i in range(size, len(num)):#形成窗口后
            if deque[0] == num[i -size]:
                deque.popleft()
            while deque and deque[-1] < num[i]:
                deque.pop()
            deque.append(num[i])
            res.append(deque[0])
        return res


if __name__ == '__main__':
    s = Solution()
    num = [10,14,12,11]
    size = 5
    print(s.maxInWindows(num, size))