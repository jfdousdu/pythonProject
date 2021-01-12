'''
第一次出现一次的字符位置
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
'''
#个人认为用词典做题会不会更好
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         n = len(s)
#         if n <0 or n > 10000:
#             return
#         #建立一个词典
#         strdic = {}
#         for i in s:
#             if i in strdic:
#                 strdic[i] =  strdic[i]+1
#             else:
#                 strdic[i] = 1
#         for i in s:
#             if strdic[i] == 1:
#                 t = s.index(i)
#                 return t
#         return -1

#别人家的思路，创建哈希表，下标为ACII值，值出现的次数
class Solution:
    def FirstNotRepeatingChar(self, s):
        # 建立哈希表,有256个字符，于是创建一个长度为256的列表
        ls = [0]*256
        for i in s:
            ls[ord(i)] += 1
        for j in s:
            if ls[ord(j)] == 1:
                return s.index(j)
        return  -1


# #直接利用count进行求解
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         if not s:
#             return -1
#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 return i
#         return  -1

if __name__ == '__main__':
    sol = Solution()
    s = "googl"
    a = sol.FirstNotRepeatingChar(s)
    print(a)