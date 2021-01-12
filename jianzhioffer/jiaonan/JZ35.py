'''
数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
对于50%50\%50%的数据,size≤104size\leq 10^4size≤104
对于75%75\%75%的数据,size≤105size\leq 10^5size≤105
对于100%100\%100%的数据,size≤2∗105size\leq 2*10^5size≤2∗105
'''

#自己写的算法时间复杂度超时（暴力求解法）方法太low了
# class Solution:
#     def InversePairs(self, data):
#         number = len(data)
#         count = 0
#         for i in range(0,number):
#             for j in range(i+1,number):
#                 if data[i] > data[j]:
#                     count += 1
#         count = count%1000000007
#         return count

#if __name__ == '__main__':
#     s = Solution()
#     data = [7,5,6,4]
#     a = s.InversePairs(data)
#     print(a)

#分治而治
class Solution:
    def InversePairsa(self, data):
        size = len(data)
        if size < 2:
            return 0

        temp = [0 for _ in range(size)]
        return self.count_reverse_pairs(data, 0, size-1, temp)

    def count_reverse_pairs(self, data, left, right, temp):
        if left == right:
            return  0

        mid = left + (right - left)/2
        left_pairs = self.count_reverse_pairs(data, left, mid, temp)
        right_pairs = self.count_reverse_pairs(data, mid+1, right, temp)
        reverse_pairs = left_pairs + right_pairs

        if data[mid] <= data[mid+1]:
            # 此时不用计算横跨两个区间的逆序对，直接返回
            # reverse_pairs
            # 为什么不用？当前if条件满足时，说明[mid + 1, right]所有数字都比[left, mid]的大，继续计算横跨逆序对没有意义，相当于剪枝。
            # print("reverse only", left, mid, right, left_pairs, right_pairs)
            return  reverse_pairs

        reverse_cross_pairs = self.merge_and_count(data, left, mid, right, temp)
        return reverse_pairs + reverse_cross_pairs

    def merge_and_count(self, data, left, mid, right, temp):
        for i in range(left, right+1):
            temp[i] = data[i]

        i = left
        j = mid+1
        res = 0
        for k in range(left,right+1):
            if i > mid:
                data[k] = temp[j]
                j += 1
            elif j > right:
                data[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                data[k] = temp[i]
                i += 1
            else:
                data[k] = temp[j]
                j += 1
                res += (mid - i + 1)
        return res

if __name__ == '__main__':
    s = Solution()
    data = [1,2,3,4,5,6,7,0]
    a = s.InversePairsa(data)
    print(a)


