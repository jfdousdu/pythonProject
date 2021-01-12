'''
连续子数组的最大和
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,
常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
'''

'''
其它思路：
正负数都有的情况，需要两个变量，一个global_max从全局来看，每次最大的是什么组合，另一个是local_max,
和global_max相比，更新global_max
'''

class Solution:
    def FindGreatestSumOfSubArray(self, arry):
        n = len(arry)
        greatestList = []
        for i in range(0,n):
            sum = 0
            for j in range(i, n):
                sum = sum +arry[j]
                greatestList.append(sum)
        return max(greatestList)

    def maxSubArray(self, nums):
        if max(nums) < 0:
            return max(nums)

        local_max, global_max = 0, 0
        for i in nums:
            local_max = max(0, local_max + i)
            global_max = max(global_max, local_max)
            print(i, local_max, global_max)
        return global_max


if __name__ == '__main__':
    s = Solution()
    a = s.FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])
    b = s.maxSubArray([1, -2, 3, 10, -4, 7, 2, -5])
    print(b)

