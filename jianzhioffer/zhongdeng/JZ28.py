'''
数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        m = len(numbers)
        n = int(m/2)+1

        for i in numbers:
            tmp = 0
            for j in range(0, m):
                if i == numbers[j]:
                    tmp = tmp + 1
                    if tmp >= n:
                        return i
        return 0

if __name__ == '__main__':
    s = Solution()
    a = s.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3])
    print(a)