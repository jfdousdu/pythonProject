'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39
斐波那契兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……在数学上，斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）
'''

#算法的复杂度较高
# class Solution:
#     def Fibonacci(self, n):
#         if n>= 39:
#             return
#         if n==0:
#             return 0
#         if n==1:
#             return 1
#         return self.Fibonacci(n-1)+self.Fibonacci(n-2)
#
# if __name__ == '__main__':
#     t = 4
#     s = Solution()
#     b = s.Fibonacci(t)
#     print(b)

# class Solution: #应该也有bug
#     def Fibonacci(self, n):
#         if n <= 0:
#             return 0
#         a = b = 1
#         for i in range(2,n):
#             a,b = b,a+b
#         return b
# # -- codingutf-8 --
class Solution:
    def Fibonacci(self, n):
        # write code here
        f = [0,1]
        for i in range(2,n+1): #range(m,n)，m<n输出：[m,m+1,..,n-1]（从m到n-1的一个list，不包括n）
            f.append(f[i-1] +f[i-2])
        return f[n]

if __name__ == '__main__':
    t = 5
    s = Solution()
    b = s.Fibonacci(t)
    print(b)