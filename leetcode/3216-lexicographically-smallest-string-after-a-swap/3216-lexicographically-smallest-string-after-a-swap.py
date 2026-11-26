class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(1, len(s)):
            slist = list(s)
            s1 = int(slist[i - 1])
            s2 = int(slist[i])
            if (s1 % 2 == 0) == (s2 % 2 == 0):
                # print(s1, s2)
                slist[i - 1], slist[i] = slist[i], slist[i - 1]
            elif (s1 % 2 != 0) == (s2 % 2 != 0):
                # print(s1, s2)
                slist[i - 1], slist[i] = slist[i], slist[i - 1]
            t = ''.join(slist)
            if t < s:
                return t
        return s