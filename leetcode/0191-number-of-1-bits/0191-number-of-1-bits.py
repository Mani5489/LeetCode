class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)
        counts = 0
        for i in bits:
            if i == '1':
                counts +=1
        return counts