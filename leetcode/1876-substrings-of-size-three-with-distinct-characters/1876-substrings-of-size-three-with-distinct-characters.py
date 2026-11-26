class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = []
        for i in range(len(s)):
            n = s[i:i + 3]
            if len(n) == 3 and len(set(n)) == 3:
                c.append(n)
        return len(c)