class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for i in t:
            result = dict1.get(i, 0)
            # print(result)
            if result == 0:
                return False
            else:
                dict1[i] -= 1
        return all(dict1[x] == 0 for x in dict1)
        