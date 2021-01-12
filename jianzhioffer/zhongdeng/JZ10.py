'''
矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法：
'''
class Solution:
    def rectCover(self, number):
        typeNumber = [0,1,2,3]
        for i in range(4, number+1):
            typeNumber.append(typeNumber[i-1]+typeNumber[i-2])
        return typeNumber[number]

if __name__ == '__main__':
    number = 13
    s = Solution()
    typeNumber = s.rectCover(number)
    print(typeNumber)
