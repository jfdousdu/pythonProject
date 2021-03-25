'''
构建乘积数组
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
对于A长度为1的情况，B无意义，故而无法构建，因此该情况不会存在。
'''
# class Solution:
#     def multiply(self, A):
#         B = [1]*len(A)  #python中l=[1]*len(seq)  l = [1,1,1] l = [1] * 3 //即[1] * 倍数
#         front = 1
#         tail =1
#         if len(A) is 1:
#             return
#         for i in range(0,len(A)):
#             if i>0:
#                 front *= A[i-1]
#                 tail *= A[len(A)-i]
#             B[i] *= front
#             B[len(A)-i-1] *= tail
#         return B
#
# if __name__ == '__main__':
#


