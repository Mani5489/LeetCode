class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = {}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i], 0) + 1
        freq = dict(sorted(freq.items(), key=lambda x: x[1]))
        nl = len(freq.values())
        n = list(freq.keys())
        t = 0
        i = 0
        while nl > k:
            v = freq.get(n[i])
            freq.pop(n[i])
            t += v
            nl -= 1
            i += 1
        return t