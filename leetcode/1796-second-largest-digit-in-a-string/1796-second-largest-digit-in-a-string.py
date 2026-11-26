class Solution:
    def secondHighest(self, s: str) -> int:
        d = set()
        for i in s:
            if i.isdigit():
                d.add(int(i))
        return sorted(d,reverse=True)[1] if d and len(d) > 1 else -1