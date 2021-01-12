'''
和为s的两个数字
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
# class Solution:
#     def FindNumbersWithSum(self, array, tsum):
#         number = len(array)
#         listValue = []
#         number1 = None
#         number2 = None
#         multiValue = 10000000000
#         for i in range(0, number):
#             for j in range(i+1,number):
#                 if tsum == array[i]+array[j]:
#                     if array[i]*array[j] < multiValue:
#                         number1 = array[i]
#                         number2 = array[j]
#                         multiValue = number1*number2
#                         print(multiValue,number1,number2)
#
#         if multiValue > 0 and  multiValue != 10000000000:
#             listValue.append(number1)
#             listValue.append(number2)
#             return listValue
#         else:
#             return []

#由于是排好的数组，所以对于和相等的两个数来说，
# 相互之间的差别越大，那么乘积将越小，
# 因此我们使用两个指针，一个从前往后遍历另一个从后往前遍历
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        i = 0
        j = len(array) -1
        while i < j:
            if array[i] + array[j] > tsum:
                j -= 1
            elif array[i] + array[j] < tsum:
                i += 1
            else:
                return [array[i], array[j]]
        return []

if __name__ == '__main__':
    s = Solution()
    array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    tsum = 21
    a = s.FindNumbersWithSum(array, tsum)
    print(a)

