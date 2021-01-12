'''
最小的K个数
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

#本事使用sort排序速度很快但感觉面试不能用sort
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         if k == 0 or tinput == None or k > len(tinput):
#             return []
#         tinput.sort()
#         print(tinput)
#         usefulList = []
#         j = 0
#         for i in tinput:
#             if k > j:
#                 usefulList.append(i)
#                 j = j + 1
#         return usefulList

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) <  k or k == 0:
            return []
        self.buildHeap(tinput[:k],k)
        for i in range(k, len(tinput)):
            if tinput[i] > self.heap[0]:
                continue
            else:
                self.heap[0] = tinput[i]
                self.perceDown(0,k)
        return  sorted(self.heap)

    def buildHeap(self, tinput, k):
        self.heap = tinput
        for i in range(k//2, -1, -1):
            self.perceDown(i, k)

    def perceDown(self, i, k):
        temp = self.heap[i]
        while(2*i+1)<k:
            child = 2*i +1
            if(child < k-1) and self.heap[child] < self.heap[child+1]:
                child =child +1
            if temp <self.heap[child]:
                self.heap[i] = self.heap[child]
                i = child
            else:
                break
        self.heap[i] = temp

if __name__ == '__main__':
    s = Solution()
    tinput = [4,5,1,6,2,7,3,8]
    k = 4
    a = s.GetLeastNumbers_Solution(tinput, k)
    print(a)