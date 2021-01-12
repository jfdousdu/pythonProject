'''
顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
'''
中心思路:输出第一行后逆时针旋转一下后，仍然输出下一行的数据，重点在于旋转。
'''
class Solution:
    def printMatrix(self, matrix):
        n = len(matrix)
        newmatrix = []
        for i in range(0,n):
            matrix.append(matrix[i])

class Solution:
    def printMatrix1(self, matrix):
        res = []
        n = len(matrix)
        m = len(matrix[0])  #此处是行与列相关的概念
        if m ==1 and n==1:
            res = [matrix[0][0]]
            return res
        else:
            for o in range((min(m,n)+1)//2):  #	取整除 - 返回商的整数部分（向下取整）
                [res.append(matrix[o][i]) for i in range(o,m-o)]
                [res.append(matrix[j][m-o-1]) for j in range(o,n-o) if matrix[j][m-o-1] not in res]
                [res.append(matrix[n-o-1][k]) for k in range(m-1-o,o-1,-1) if matrix[n-o-1][k] not in res]
                [res.append(matrix[l][o]) for l in range(n-1-o,o-1,-1) if matrix[l][o] not in res]
            return res

    def printMatrix(self,matrix):






matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(matrix[1][1])
s = Solution()
a = s.printMatrix(matrix)
print(a)