class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)
        t = 0
        for i in jewels:
            t += s.get(i,0)
        return t