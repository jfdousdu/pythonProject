'''
数组中只出现一次的数字
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
'''
#我的方法比较复杂，题目给出的方法十分巧妙
class Solution:
    def FindNumsAppearOnce(self, array):
        if len(array) < 2:
            return array
        array = sorted(array)
        onceList = []
        for i in range(0, len(array)):
            if i == 0:
                if array[i] != array[i+1]:
                    onceList.append(array[i])
            elif i == len(array)-1:
                if array[i] != array[i-1]:
                    onceList.append(array[i])
            else:
                if array[i]!=array[i-1] and array[i]!=array[i+1]:
                    onceList.append(array[i])
        return onceList

if __name__ == '__main__':
    s = Solution()
    array = [2,4,3,6,3,2,5,5]
    a = s.FindNumsAppearOnce(array)
    print(a)