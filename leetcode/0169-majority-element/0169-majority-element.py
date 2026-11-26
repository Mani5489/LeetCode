class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        if n==0:
            return nums[0]
        majorElement = 0
        dict1 = {}
        for i in nums[:]:
            dict1[i] = dict1.get(i, 0) + 1
        for key, values in dict1.items():
            if values >= n:
                majorElement = key
        return majorElement

        