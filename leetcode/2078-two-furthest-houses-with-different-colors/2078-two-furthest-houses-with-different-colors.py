class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        s1, e1 = 0, len(colors) - 1
        s2, e2 = 0, len(colors) - 1
        m1, m2 = 0, 0
        while s1 < e1:
            if colors[s1] != colors[e1]:
                if m1 < (e1 - s1):
                    m1 = e1 - s1
            s1 += 1
        while e2 > s2:
            if colors[e2] != colors[s2]:
                if m2 < (e2 - s2):
                    m2 = e2 - s2
            e2 -= 1
        return max(m1, m2)

        