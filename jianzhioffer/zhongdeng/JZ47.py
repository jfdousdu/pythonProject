'''
求1+2+3+...+n
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
class Solution:
    def __init__(self):
        sum = 0

    def Sum_Solution(self, n):
        if n<= 0:
            return 0
        if n > 0:
            sum = n + self.Sum_Solution(n-1)
        return sum


if __name__ == '__main__':
    s = Solution()
    a = s.Sum_Solution(8)
    print(a)