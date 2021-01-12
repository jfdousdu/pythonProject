'''
表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
# class Solution:
#
#     def isNumeric(self, s):
#         news = str(s)
#         if news.count(".")>1:
#             return  False
#
#         for j in range(len(news)-1):
#             if news[j]=='+' and news[j+1]=='-':
#                 return False
#             if news[j] == '+' and news[j + 1] == '+':
#                 return False
#             if news[j] == '-' and news[j + 1] == '+':
#                 return False
#             if news[j] == '-' and news[j + 1] == '-':
#                 return False
#             if news[j+1] == ord('e') and j==len(news)-2:
#                 return False
#
#         for i in s:
#             if ord(i) >= ord('a') and ord(i) < ord('e'):
#                 return False
#
#         return True
有问题

class Solution:
    def isNumeric(self, s):
        hasE = False
        hasDot = False
        hasSign = False
        for i in range(len(s)):
            if s[i] == 'e'  or s[i] =='E':
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasDot or hasE: #此处有问题
                    return False
                hasDot = True
            elif s[i] == '+' or s[i] == '-':
                if hasSign and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                if not hasSign:
                    if i != 0 and s[i-1]!= 'e' and s[i-1]!= 'E':
                        return False
                hasSign=True
            else:
                if s[i] < '0' or s[i] >'9':
                    return False
        return True


