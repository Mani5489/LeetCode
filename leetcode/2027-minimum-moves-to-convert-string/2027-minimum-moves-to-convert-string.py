class Solution:
    def minimumMoves(self, s: str) -> int:
        m = 0
        slist = list(s)
        i = 0
        while i < len(slist):
            if slist[i] == 'X':
                slist[i:i + 3] = ['0' for i in slist[i:i + 3]]
                m += 1
            i += 1
        return m
        