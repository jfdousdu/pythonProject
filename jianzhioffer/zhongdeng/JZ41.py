'''
和为S的连续正数序列
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
'''
# class Solution:
#     def FindContinuousSequence(self, tsum):
#         tmp = int(tsum/2)
#         resultList = []
#         for i in range(1, tmp+2):
#             sum = 0
#             j = i
#             count = 0
#             oneResultList = []
#             while sum < tsum:
#                 sum = sum + j
#                 j = j + 1
#                 count = count + 1
#             if count < 2:
#                 return resultList
#             if sum == tsum:
#                 for k in range(i ,i+count):
#                     oneResultList.append(k)
#                 resultList.append(oneResultList)
#         return resultList

class Solution:
    def FindContinuousSequence(self, tsum):
        i = 1
        j = 1
        sum = 0
        res = []

        while i <= tsum//2:
            if sum < tsum:
                sum += j
                j += 1
            elif sum > tsum:
                sum -= i
                i += 1
            else:
                arr = list(range(i,j))#注意此处是加一的判断
                res.append(arr)
                sum -= i
                i += 1
        return  res

if __name__ == '__main__':
    s = Solution()
    a = s.FindContinuousSequence(9)
    print(a)