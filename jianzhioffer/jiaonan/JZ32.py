'''
把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

#介绍一个新的函数cmp_to_key为比较函数
# from functools import cmp_to_key
# L=[9,2,23,1,2]
#
# sorted(L,key=cmp_to_key(lambda x,y:y-x))
# 输出：
# [23, 9, 2, 2, 1]
#
# sorted(L,key=cmp_to_key(lambda x,y:x-y))
# 输出：
# [1, 2, 2, 9, 23]


# class Solution:
#     def PrintMinNumber(self, numbers):
#         if not numbers:
#             return ""
#
#         list = [str(x) for x in numbers]
#         list.sort(cmp = lambda x, y:cmp(x+y,y+x))  #python 2.X
#         return  int("".join(list))

# class Solution:
#     def PrintMinNumber(self, numbers):
#         if not numbers:
#             return ""
#
#         list = [str(x) for x in numbers]
#         list.sort(cmp = self.sort)  #python 2.X
#         return  int("".join(list))
#
#     def sort(self, x, y):
#         if x + y > y + x:
#             return 1
#         if x + y  == y + x:
#             return 0
#         else:
#             return -1

class Solution:
   def compare(self, x,y): #self 颜色和x的颜色不同
       return x+y > y+x

   def PrintMinNumber(self, numbers):
        numbers = [str(nums) for nums in numbers]
        for i in range(len(numbers)):
            for j in range(len(numbers)-i-1):
                if self.compare(numbers[j], numbers[j+1]):
                    numbers[j] , numbers[j+1] = numbers[j+1], numbers[j]
        return int("".join(numbers)) # ''.join(numbers)

if __name__ == '__main__':
    s = Solution()
    numbers = [9,2,23,1,2]
    a = s.PrintMinNumber(numbers)
    print(a)
