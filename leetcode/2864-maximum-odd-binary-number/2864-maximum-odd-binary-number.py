class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        maps = Counter(s)
        Zs, Os = maps.get('0', 0), maps.get('1', 0)
        res = []
        if Os > 0:
            for x in range(Os - 1):
                res.append('1')
        if Zs > 0:
            for x in range(Zs):
                res.append('0')
        if len(s) != len(res):
            res.append('1')
        return ''.join(res)
        