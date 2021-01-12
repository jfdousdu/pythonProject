'''
正则表达式匹配
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
 在本题中，匹配是指字符串的所有字符匹配整个模式。
 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''
‘’‘’
#重点考虑转移方程的不同情况进行求解
#感觉转移方程并不好考虑
# 转移方程： 需要注意，由于 dp[0][0] 代表的是空字符的状态， 因此 dp[i][j] 对应的添加字符是 s[i - 1] 和 p[j - 1] 。
#
#     当 p[j - 1] = '*' 时， dp[i][j] 在当以下任一情况为 truetruetrue 时等于 truetruetrue ：
#         dp[i][j - 2]： 即将字符组合 p[j - 2] * 看作出现 0 次时，能否匹配；
#         dp[i][j - 1]： 即将字符组合 p[j - 2] * 看作出现 1 次时，能否匹配；
#         dp[i - 1][j] 且 s[i - 1] = p[j - 2]: 即让字符 p[j - 2] 多出现 1 次时，能否匹配；
#         dp[i - 1][j] 且 p[j - 2] = '.': 即让字符 '.' 多出现 1 次时，能否匹配；
#
#     当 p[j - 1] != '*' 时， dp[i][j] 在当以下任一情况为 truetruetrue 时等于 truetruetrue ：
#         dp[i - 1][j - 1] 且 s[i - 1] = p[j - 1]： 即让字符 p[j - 1] 多出现一次时，能否匹配；
#         dp[i - 1][j - 1] 且 p[j - 1] = '.'： 即将字符 . 看作字符 s[i - 1] 时，能否匹配；
class Solution:
    def match(self, s, pattern):
        m, n = len(s)+1, len(pattern)+1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        for j in range(2, n, 2):
            dp[0][j] = dp[0][j-2] and pattern[j-1] =='*'

        for i in range(1, m):
            for j in range(1, n):
                if pattern[j-1] == '*':
                    if dp[i][j-2]:
                        dp[i][j] = True
                    elif dp[i][j-1]:
                        dp[i][j] = True
                    elif dp[i-1][j] and s[i-1] == pattern[j-2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and pattern[j-2] == '.':
                        dp[i][j] = True
                else:
                    if dp[i-1][j-1] and s[i-1] == pattern[j-1]:
                        dp[i][j] = True
                    elif dp[i-1][j-1] and pattern[j-1] == '.':
                        dp[i][j] = True
        return dp[-1][-1]



#知乎
# 思路：如果 s和pattern都为空，匹配成功。
# 当模式中的第二个字符不是*时：
# （1）如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，然后匹配剩余的；
# （2）如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。
# 而当模式中的第二个字符是*时：
# （1）模式后移2字符，相当于x*被忽略；
# （2）字符串后移1字符，模式后移2字符。
# class Solution:
#     # s, pattern都是字符串
#     def match(self, s, pattern):
#         if s == pattern:
#             return  True
#         if len(pattern)>1 and pattern[1] == "*":
#             if s and (s[0] == pattern[0] or pattern[0] == '.'):
#                 return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
#             else:
#                 return self.match (s, pattern[2:])
#         elif s and pattern and (s[0] == pattern[0] or pattern[0] == '.'):
#             return self.match(s[1:], pattern[1:])
#         return False

if __name__ == '__main__':
    sol = Solution()
    s =  'aaa'
    pattern = "a.a"
    a = sol.match(s, pattern)
    print(a)