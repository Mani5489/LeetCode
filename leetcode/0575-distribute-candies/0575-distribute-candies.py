class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        allowed = len(candyType) // 2
        distinct = len(list(set(candyType)))
        if distinct <= allowed:
            return distinct
        else:
            return allowed