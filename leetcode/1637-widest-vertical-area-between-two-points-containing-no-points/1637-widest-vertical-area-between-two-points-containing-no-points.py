class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for i in points:
            x.append(i[0])
        x.sort()
        m = 0
        p = x[0]
        for i in range(1, len(x)):
            n = x[i]
            g = abs(p - n)
            if g > m:
                m = g
            p = n
        return m