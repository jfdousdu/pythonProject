'''
跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        stepNumber = [0,1,2]
        for i in range(3,number+1):
            stepNumber.append(stepNumber[i-1]+stepNumber[i-2])
        return stepNumber[number]

