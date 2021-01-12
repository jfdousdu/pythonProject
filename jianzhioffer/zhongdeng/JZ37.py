'''
数字在升序数组中出现的次数
统计一个数字在升序数组中出现的次数。
'''

# class Solution:
#     def GetNumberOfK(self, data, k):
#         n = len(data)
#         if n==0:
#             return 0
#         count = 0
#         tmp = int(n/2)
#         while tmp != None:
#             if data[tmp] == k:
#                 count += 1
#                 i = tmp + 1
#                 j = tmp - 1
#                 print(j,'==')
#
#                 while j>=0 and data[j] == k: #and 存在短路问题
#                     print(j, '-')
#                     j = j - 1
#                     count = count + 1
#                     print(count, "--")
#
#                 while  i<=n-1 and data[i] == k:
#                     print(i,"+")
#                     i = i+1
#                     count = count+1
#                     print(count,"++")
#             return count
#
#             if data[tmp] > k:
#                 tmp = int(tmp/2)
#             else:
#                 tmp = int((tmp + n)/2)
#         return

class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        i = 0
        j = len(data) - 1
        while i < j and data[i] != data[j]:
            if data[i] < k:
                i += 1
            if data[j] > k:
                j -= 1
        if data[i] != k:
            return 0
        return j-i+1


if __name__ == '__main__':
    s = Solution()
    data = [2,3,3,3,3,3]
    k = 3
    a = s.GetNumberOfK(data, k)
    print(a)