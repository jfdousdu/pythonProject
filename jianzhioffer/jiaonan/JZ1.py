'''
二维数组中的查找
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    def Find(self, target, array):
        n = len(array)
        for i in range(0, n):
            if target in array[i]:
                return True
        return False

# class Solution:
#     def Find(self, target, array):
#         rows = len(array) - 1
#         cols = len(array[0]) - 1
#         i = rows
#         j = 0
#         while j <= cols and i >= 0:
#             if target < array[i][j]:
#                 i-=1
#             elif target > array[i][j]:
#                 j += 1
#             else:
#                 return True
#         return False



if __name__ == '__main__':
    s = Solution()
    target = 15
    array = [[1,2,8,9],[2,4,9,12],[4,10,13],[6,8,11,15]]
    a = s.Find(target, array)
    print(a)
