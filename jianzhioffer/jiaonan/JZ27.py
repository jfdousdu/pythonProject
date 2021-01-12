'''
字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''
#此题没有明白

# class Solution:
#     def Permutation(self, ss):
#         if len(ss) == 0 or len(ss) == 1:
#            return ss
#         res = []
#         c = list(ss)
#         def dfs(x):
#             if x == len(c) -1:
#                 res.append(''.join(c))
#                 return
#             dic = set()
#             for i in range(x, len(c)):
#                 if c[i] in dic:continue
#                 dic.add(c[i])
#                 c[i], c[x] = c[x], c[i]
#                 dfs(x+1)
#                 c[i], c[x] = c[x], c[i]
#         dfs(0)
#         return res

#思路：递归，把字符串分为两部分：字符串的第一个字符，第一个字符后面的所有字符。
#1.求所以可能出现在第一个位置的字符，用索引遍历。
#2.求第一个字符以后的所有字符的全排列。将后面的字符又分成第一个字符以及剩余的字符。
class Solution:
    def Permutation(self, ss):
        if len(ss) == 0 or len(ss) == 1:
            return ss
        res = []
        self.helper( ss, res,'')
        return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:  #这里不明白
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i]+ss[i+1:],res,path+ss[i])

if __name__ == '__main__':
    s = Solution()
    ss = 'abc'
    a = s.Permutation(ss)
    print(a)