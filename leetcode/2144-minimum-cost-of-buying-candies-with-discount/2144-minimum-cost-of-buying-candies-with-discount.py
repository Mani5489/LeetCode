class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        if len(cost) <= 2:
            return sum(cost)
        i = 0
        t = 0
        while i < len(cost):
            c = 2
            j = 0
            while j < c and i < len(cost):
                t += cost[i]
                j += 1
                i += 1
            i += 1
        return t
        