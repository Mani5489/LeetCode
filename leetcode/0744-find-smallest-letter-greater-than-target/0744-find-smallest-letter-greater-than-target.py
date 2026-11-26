class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters)
        close = len(letters)
        while low <= high:
            try:
                mid = (low + high) // 2
                if letters[mid] > target:
                    close = mid
                    high = mid - 1
                else:
                    low = mid + 1
            except IndexError:
                return letters[0]

        return letters[close]
        