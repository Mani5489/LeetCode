class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        allThree = list(set(nums1) & set(nums2) & set(nums3))
        allTwo1 = list(set(nums1) & set(nums2))
        allTwo2 = list(set(nums2) & set(nums3))
        allTwo3 = list(set(nums3) & set(nums1))
        return list(set(allThree+allTwo1+allTwo2+allTwo3))