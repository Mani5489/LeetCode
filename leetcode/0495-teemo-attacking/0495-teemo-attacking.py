class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        left = 0
        right = left + 1
        total = 0
        while right < len(timeSeries):
            if (timeSeries[right] - timeSeries[left]) >= duration:
                total += duration
                # print(total)
            else:
                total += timeSeries[right] - timeSeries[left]
                # print(total)
            left = right
            right += 1
        return total + duration
        