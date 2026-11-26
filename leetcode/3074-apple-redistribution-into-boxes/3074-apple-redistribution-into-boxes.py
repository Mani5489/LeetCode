class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t = sum(apple)
        capacity.sort(reverse=True)
        c = 0
        i = 0
        while c < t:
            c += capacity[i]
            i += 1
        return i
        