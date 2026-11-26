class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}
        for i in range(1, n + 1):
            c = sum(map(int, str(i)))
            if c in freq.keys():
                v = freq.get(c, 0) + 1
                freq[c] = v
            else:
                freq[c] = 1
        m = max(freq.items(), key=lambda x: x[1])[1]
        freq = dict(filter(lambda x: x[1] == m, freq.items()))
        return len(freq)