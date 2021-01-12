'''
把字符串转换成整数
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0
'''
class Solution:
    def StrToInt(self,s):
        flag = 1
        number = 0
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            s = s[1:]
            flag = -1
        elif s[0] == '+':
            s = s[1:]
            flag = 1

        ###s[1]=='4':
        ##print(print(type(s)))
        ##<class 'str'>

        for i in s:
            if i >= '0' and i<='9':
                number =int(i) + number*10
            else:
                return False
        number = flag*number
        return number

if __name__ == '__main__':
    sol = Solution()
    s = '444a'
    s1 = '-476'
    s2 = '+124'
    s3 = '4447'
    a = sol.StrToInt(s)
    a1 = sol.StrToInt(s1)
    a2 = sol.StrToInt(s2)
    a3 = sol.StrToInt(s3)
    print(a)
    print(a1)
    print(a2)
    print(a3)




