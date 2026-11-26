class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = hash.get(nums[i], 0) + 1
        duplicate = 0
        for i, j in hash.items():
            if j > 1:
                duplicate = i
        expectedSum = 0
        for i in range(1, len(nums) + 1):
            expectedSum += i
        missing = expectedSum - (sum(nums) - duplicate)
        return [duplicate, missing]

        