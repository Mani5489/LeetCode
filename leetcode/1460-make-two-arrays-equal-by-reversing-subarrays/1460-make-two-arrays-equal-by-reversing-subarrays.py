class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter

        return Counter(target) == Counter(arr)

        