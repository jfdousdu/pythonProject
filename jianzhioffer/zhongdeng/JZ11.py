'''
二进制中1的个数
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
'''
class Solution:
    def NumberOf1(self, n):
      return bin(n&0xffffffff).count('1')

    def NumberOf2(self, n):
      count = 0
      while n&0xffffffff != 0:
           count += 1
           n = n & (n-1)#判断一个整数二进制中有多少个1
           # n & (n - 1)将n的二进制表示中的最低位为1的改为0
      return count

s = Solution()
print(s.NumberOf2(-9))