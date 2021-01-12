'''
字符流中第一个不重复的字符
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
'''
#用一个字典保存出现过的字符，以及字符出现的次数
# class Solution:
#     def __init__(self):
#         self.s = ''
#         self.dict1 = {} #字典
#
#     def FirstAppearingOnce(self):
#         for i in self.s:
#             if self.dict1[i] == 1:
#                 return i
#         return '#'
#
#     def Insert(self, char):
#         self.s = self.s + char
#         print(char,self.s,self.dict1)
#         if char in self.dict1:
#             self.dict1[char] = self.dict1[char] +1
#         else:
#             self.dict1[char] = 1

class Solution:
    def __init__(self):
        self.array = []
        self.result = []

    def FirstAppearingOnce(self):
        if len(self.result) != 0:
            for i in self.result:
                return i
        return '#'

    def Insert(self, char):
        for i in char:
            if i in self.result:
                self.result.remove(i)
            elif i not in self.array:
                self.result.append(i)
            self.array.append(i)

if __name__ == '__main__':
    s = Solution()
    for i in 'ggoole':
        s.Insert(i)
    a = s.FirstAppearingOnce()
    print(a)