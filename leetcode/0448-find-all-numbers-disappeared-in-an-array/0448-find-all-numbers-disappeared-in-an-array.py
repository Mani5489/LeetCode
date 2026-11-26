class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        set2 = set()
        for i in range(1, len(nums) + 1):
            set2.add(i)
        return list(set2.difference(set1))


