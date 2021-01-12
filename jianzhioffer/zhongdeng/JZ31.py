'''
整数中1出现的次数（从1到n整数中1出现的次数）
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
'''

class Solution:
    def NumberOf1Between1AndN_Solution(self,n):
        number = 0
        for i in range(1, n+1):
            j = i
            while j>0:
                if j%10 == 1:
                   number += 1
                j = j/10
        return number


if __name__ == '__main__':
    s = Solution()
    a1 = s.NumberOf1Between1AndN_Solution(11)
    a2 = s.NumberOf1Between1AndN_Solution(10)
    a3 = s.NumberOf1Between1AndN_Solution(131)
    print(a1,a2,a3)
