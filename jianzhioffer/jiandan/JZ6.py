''''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
#这种不能锻炼能力，肯定不行
class Solution:
    def minNumberInRotateArray(self,rotateArray):
        return min(rotateArray)

s = Solution()
a = s.minNumberInRotateArray([2,4,5,0,10])
print(a)
'''

class Solution:
    def minNumberInRotateArray(self,rotateArray):
        for i in range(0,len(rotateArray)-1):
            if rotateArray[i]>rotateArray[i+1]:
                return rotateArray[i+1]

s = Solution()
a = s.minNumberInRotateArray([2,3,5,1,2])
print(a)
print(s.minNumberInRotateArray([3,4,7,2,3]))


