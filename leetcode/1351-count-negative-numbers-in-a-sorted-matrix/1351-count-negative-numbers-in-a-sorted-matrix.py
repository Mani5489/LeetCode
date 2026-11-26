class Solution:
    def findNeg(self, list1):
        low = 0
        high = len(list1) - 1
        count = 0
        while low <= high:
            mid = (low + high) // 2
            if list1[mid] < 0:
                count += 1
                high = mid - 1
            else:
                low = mid + 1
        # print(len(list1), low)
        return len(list1) - low

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            count += Solution().findNeg(i)
        return count