'''替换空格'''
'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

class Solution:
    def replaceSpace(self, s):
        news = ''
        for i in s:
            if i ==' ':
               news = news + '%20'
            else:
               news = news + i
        return news

if __name__ == '__main__':
    s = Solution()
    string = "We Are Happy"
    a = s.replaceSpace(string)
    print(a)