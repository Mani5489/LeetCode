class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = {}
        for i in t:
            hash[i] = hash.get(i, 0) + 1
        # print(hash)
        for i in s:
            if hash[i] >= 1:
                hash[i] = hash.get(i, 0) - 1
        # print(hash)
        return ''.join([x for x in hash if hash[x] >= 1])

        