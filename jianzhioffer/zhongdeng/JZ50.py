'''
数组中重复的数字
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中第一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
返回描述：
如果数组中有重复的数字，函数返回true，否则返回false。
如果数组中有重复的数字，把重复的数字放到参数duplication[0]中。（ps:duplication已经初始化，可以直接赋值使用。）
'''
class Solution:
    def duplicate(self, numbers, duplication,duplication1):
        n = len(numbers)
        for i in numbers:
            t = numbers.index(i)
            for j in range(t+1, n):
                if i == numbers[j]:
                    duplication.append(i)
                    duplication1[0] = i  #此处的区别和联系是什么
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    numbers = [2,1,3,1,4]
    duplication = []
    duplication1= [0]
    a = s.duplicate(numbers,duplication, duplication1)
    print(a)
    print(duplication[0])
    print(duplication1)