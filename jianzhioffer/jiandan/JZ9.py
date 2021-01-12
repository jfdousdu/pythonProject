'''
变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
动态规划问题
f(n)=f(n-1)*2
'''''
#牛客网自己的平台规定了函数的参数所以我们要遵守不然会出现错误

class Solution:
    def jumpSolution(self,totalNumber):
        if totalNumber <=0: return 0
        if totalNumber == 1: return 1
        if totalNumber == 2: return 2
        result = [1,2]
        for i in range(2,totalNumber):
            result.append(result[i-1]*2)
            #print(result[-1])表现数组最后一位
        return result[totalNumber-1]  #return是跳出循环后我们要注意排版

'''
class Solution:
    def jumpFloorII(self, number):
        if number <= 0:  return 0
        if number == 1: return 1
        if number == 2: return 2
        result = [1,2]
        for i in range(2,number):
            result.append(2*result[-1])
        return result[-1]
'''
s = Solution()
t = Solution  #这种情况下，会寻找不到self，故要多编辑一下
a = s.jumpSolution(2)
b = t.jumpSolution(t,totalNumber=9)
print(a,b,)