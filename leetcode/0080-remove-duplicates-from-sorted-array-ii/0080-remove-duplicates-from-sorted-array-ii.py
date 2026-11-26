class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list1 = []
        dictCount = {}
        for i in nums:
            dictCount[i] = dictCount.get(i, 0) + 1
            if dictCount[i] <= 2:
                list1.append(i)
        nums[:] = list1.copy()
        return len(nums)