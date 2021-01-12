'''
数值的整数次方
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
'''
import math
class Solution:
    # def Power1(self, base, expoment):
    #     if expoment:
    #         self.expoment  = float(expoment)
    #     if base!= 0 or expoment != 0:
    #         return base**expoment #借助现有的运算符进行求解，结果将相对简单

    # class Solution:
    #     def Power(self, base, expoment):
    #         a = 1
    #         if base != 0 or expoment != 0:
    #             if expoment == 0:
    #                 return 1
    #             if base == 0:
    #                 return 0
    #             while expoment > 0:
    #                 a = a * base
    #                 expoment = expoment - 1
    #             if expoment < 0:
    #                 abs_expoment = abs(expoment)
    #                 while abs_expoment > 0:
    #                     a = base * a
    #                     abs_expoment = abs_expoment - 1
    #                 return 1 / a
    #             return a  #注意return的相关对应

    def Power(self, base, expoment):
        a = 1
        if base != 0 or expoment != 0:
           if expoment == 0:
               return  1
           if base == 0:
               return  0
           if expoment < 0:
               abs_expoment = abs(expoment)
               while abs_expoment > 0:
                   a = base * a
                   abs_expoment = abs_expoment-1
               return 1/a
           while expoment > 0:
               a = a * base
               expoment = expoment - 1
           return a


n = 2
m = -3

s = Solution()
a = s.Power(n, m)
print(a)
