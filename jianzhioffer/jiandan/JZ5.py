'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
利用两个数组
'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,node):
        self.stack1.append(node)
    def pop(self):
        if not self.stack1:
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res


s=Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop(),s.pop(),s.pop(),s.pop())