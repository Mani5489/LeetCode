class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maps = {}
        lens = []
        for idx in range(len(s)):
            c = s[idx]
            if c in maps:
                v = idx - maps.get(c, 0) - 1
                lens.append(v)
            else:
                maps[c] = idx
        return max(lens) if lens else -1