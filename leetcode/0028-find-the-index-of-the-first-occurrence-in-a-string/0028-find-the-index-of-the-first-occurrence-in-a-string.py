class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        indexList = []
        if haystack == needle:
            return haystack.index(haystack[0])
        while (i + len(needle)) <= len(haystack):
            new = haystack[i:i + len(needle)]
            i += 1
            if new.startswith(needle):
                indexList.append(i-1)
            else:
                indexList.append(-1)
        val = list(filter(lambda x: x >= 0, indexList))
        if val:
            return val[0]
        else:
            return -1
        