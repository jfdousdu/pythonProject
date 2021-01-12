'''
翻转单词顺序列
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。
后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''
# class Solution:
#     def ReverseSentence(self, s):
#         newList = []
#         newList = s.split(' ')
#         reList = []
#         n = len(newList)
#         num = int(n/2)
#         for i in range(0,num):
#             newList[i], newList[n-1-i] = newList[n-1-i], newList[i]
#         return ' '.join(newList)

class Solution:
    def ReverseSentence(self, s):
        if s is None or len(s) == 0:
            return s
        stack = []
        for i in s.split(' '):
            stack.append(i)
        res = ""
        print(res)
        while len(stack) > 0:
            res += stack.pop()+" "
        res = res[:-1] #res[:-1]其实就是去除了这行文本的最后一个字符（换行符）后剩下的部分。
        return res


if __name__ == '__main__':
    s = Solution()
    string = "student. a am I"
    a = s.ReverseSentence(string)
    print(a)