'''
不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
'''
与其它知识点相关联
对于数字做运算，除了加减乘除外，还有位运算，位运算是针对二进制的，位运算分三个步骤：
各位相加但不进位
计算进位值
把前两步的结果相加，将结果转化为十进制
&按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
^按位异或运算符：当两对应的二进位相异时，结果为1
~按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
<<左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
这个不明白
'''

class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            sum = num1^num2
            carry = (num1&num2)<<1
            num1 = sum
            num2 = carry
        return num1


# class Solution:
#     def Add(self, num1, num2):
#         while num2:
#             sum = num1 ^ num2
#             carry = 0xFFFFFFFF&(num1 & num2)<<1
#             carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
#             num1 = sum
#             num2 = carry
#         return num1

s = Solution()
a = s.Add(-3,-4)
print(a)