class Solution:
    def createSet(self, arr1: List[int]) -> list[list[str]]:
        hashDict = {}
        for i in arr1:
            strVal = str(i)
            list1 = []
            for j in range(1, len(strVal) + 1):
                list1.append(strVal[:j])
                hashDict[i] = list1
        return list(hashDict.values())

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(set(arr1))
        arr2 = list(set(arr2))
        dict1 = Solution().createSet(arr1)
        dict2 = Solution().createSet(arr2)
        a_list = {int(num) for sublist in dict1 for num in sublist}
        b_list = {int(num) for sublist in dict2 for num in sublist}
        common = a_list & b_list
        # print(len(str(max(common, default=0))))
        return len(str(max(common))) if common else 0