class Solution:
    def range(self, i, arr2: List[int]):
        low = 0
        high = len(arr2) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr2[mid] >= i:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for i in arr1:
            low = Solution.range(self, i - d, arr2)
            if low < len(arr2) and arr2[low] <= i + d:
                continue
            else:
                count += 1
        return count