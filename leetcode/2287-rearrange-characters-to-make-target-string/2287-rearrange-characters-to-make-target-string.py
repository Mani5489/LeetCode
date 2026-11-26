class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sdict = {}
        targetDict = {}
        for i in range(len(s)):
            sdict[s[i]] = sdict.get(s[i], 0) + 1
        for i in range(len(target)):
            targetDict[target[i]] = targetDict.get(target[i], 0) + 1
        occurrence = [sdict.get(k, 0) // v for k, v in targetDict.items()]
        return min(occurrence, default=0)



        