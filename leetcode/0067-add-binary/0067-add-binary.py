class Solution(object):
    def addBinary(self, a, b):
        def toNum(num):
            sumValue = 0
            list1 = list(str(num))[::-1]
            for i in range(len(list1)):
                sumValue = sumValue + int(list1[i]) * 2 ** int(i)
            return sumValue

        valueA = toNum(a)
        valueB = toNum(b)
        return str(bin(valueA + valueB)[2:])