class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        i = 0
        j = len(s)
        for k in s:
            if k == 'I':
                res.append(i)
                i += 1
            elif k == 'D':
                res.append(j)
                j -= 1
        res.append(j)
        return res