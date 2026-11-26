class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie = 0
        child = 0
        happyChild = 0
        while (cookie < len(s)) & (child < len(g)):
            if s[cookie] >= g[child]:
                cookie += 1
                child += 1
                happyChild += 1
            else:
                cookie += 1
        return happyChild
        