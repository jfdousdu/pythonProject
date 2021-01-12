'''
包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
class Solution:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, node):
        self.A.append(node)
        if not self.B or self.B[-1] >= node:
            self.B.append(node)

    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]

if __name__ == '__main__':
    s = Solution()
    s.push(3)
    s.push(1)
    s.push(10)
    s.pop()
    a = s.min()
    print(a, s.A, s.B)