class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        longestString = ''
        subString = str(strs[0])
        for i in range(1, len(strs)):
            while len(subString) > 0:
                if strs[i].startswith(subString):
                    longestString = subString
                    break
                subString = subString[:-1]
                if not subString:
                    return ''
        return longestString

        