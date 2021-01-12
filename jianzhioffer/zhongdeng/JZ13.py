'''
 	调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reOrderArray1(self, array):
        n = len(array)
        number = 0
        while number != 1:
            for i in range(0, n-1):
                if array[i]%2 == 0 and array[i+1]%2 ==1:
                     tmp = array[i]
                     array[i] = array[i+1]
                     array[i+1] = tmp

                number = 0
                for j in range(0, n - 1):
                    if array[j] % 2 == 1 and array[j + 1] % 2 == 0:
                        number = number + 1
        return array

    def reOrderArray(self, array):
        oddList = []
        evenList = []
        n = len(array)

        for i in range(0, n):
            if array[i] % 2 == 0:
                evenList.append(array[i])
            else:
                oddList.append(array[i])
        return oddList+evenList



if __name__ == '__main__':
    s = Solution()
    array = [10,1,2,3,4,5,6,7,9]
    a = s.reOrderArray(array)
    print(a)
