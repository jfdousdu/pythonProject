'''
左旋转字符串
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，
请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
是不是很简单？OK，搞定它！
'''
class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''

        newString = []
        for i in s:
            newString.append(i)

        while n > 0:
            a = newString.pop(0)
            newString.append(a)
            n= n-1
        t = ''.join(newString) #将分开的数组进行合并，返回合并好的数值
        return t

# class Solution:
#     def LeftRoteString(self, s, n):
#         m = len(s)
#         res1 = s[n:m]
#         res2 = s[0:n]
#         res = res1+res2
#         return res



if __name__ == '__main__':
    s = Solution()
    string = '9998'
    n=3
    a = s.LeftRotateString(string, n)
    print(a)