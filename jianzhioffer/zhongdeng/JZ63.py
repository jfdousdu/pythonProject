'''
数据流中的中位数
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

#两个结构体之间的调用关系
#其实没有必要恪守这个变量好像可以增加看答案呢
# class Solution:
#     def __init__(self):
#         self.res = []
#     def Insert(self, num):
#         self.res.append(num)
#     def GetMedian(self, res):
#         if len(self.res) == 0:
#             return None
#         res.sort()
#         if len(res)%2 == 1:
#
#             return res[int(len(res)/2)]
#         else:
#             return (res[int(len(res)/2 - 1)] + res[int(len(res)/2)])/2.0
class Solution:
    def __init__(self):
        self.res = []

    def Insert(self, num):
        self.res.append(num)

    def GetMedian(self, res):
        if len(self.res) == 0:
            return None
        res = sorted(self.res)
        if len(self.res) % 2 == 1:
            return res[(len(self.res) / 2)]
        else:
            return (res[(len(self.res) / 2 - 1)] + res[(len(self.res) / 2)]) / 2.0


# class Solution:
#     def __init__(self):
#         self.dataStream = []
#     def Insert(self, num):
#             self.dataStream.append(num)
#
#     def GetMedian(self, dataStream):
#         dataStream.sort()
#         number = len(dataStream)
#         if number%2 == 1:
#             return dataStream[int((number-1)/2)]
#         else:
#             t = int(number / 2)
#             return (dataStream[t]+dataStream[t-1])/2
#
#
#
if __name__ == '__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.Insert(i)
    print(s.res)
    a = s.GetMedian(s.res)
    print(a)


# class Solution:
#     def Insert(self, num):
#         n = len(num)
#         dataStream = []
#         for i in range(0, n):
#             dataStream.append(num[i])
#         dataStream.sort()
#         return dataStream
#
#     def GetMedian(self, dataStream):
#         number = len(dataStream)
#         if number % 2 == 1:
#             return dataStream[int((number - 1) / 2)]
#         else:
#             t = int(number / 2)
#             return (dataStream[t] + dataStream[t - 1]) / 2