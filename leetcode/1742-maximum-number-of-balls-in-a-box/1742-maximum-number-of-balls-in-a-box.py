class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        freq = {}
        for i in range(lowLimit, highLimit + 1):
            v = sum(list(map(int, str(i))))
            if v not in freq:
                freq[v] = 1
            elif v in freq:
                value = freq.get(v, 0)
                freq[v] = value + 1
        return max(freq.values())