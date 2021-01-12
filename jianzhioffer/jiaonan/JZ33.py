'''
丑数
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
#分情况讨论，具体步骤并不明确
#感觉此题并不会呀
#动态规划的解法，确保数组里已有的丑数是排好序的，同时要维护三个索引
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        num_list = [1]
        i = 0
        j = 0
        k = 0
        while len(num_list) < index:
            num2, num3, num5 = num_list[i]*2, num_list[j]*3, num_list[k]*5
            num = min(num2, num3, num5)
            if num == num2:
                i += 1
            if num == num3:
                j += 1
            if num == num5:
                k += 1
            num_list.append(num)
            print(num_list)
        return num_list[index-1] #num_list[-1]

if __name__ == '__main__':
    s = Solution()
    index = 20
    a = s.GetUglyNumber_Solution(index)
    print(a)
