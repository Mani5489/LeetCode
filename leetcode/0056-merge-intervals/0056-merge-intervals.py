class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]
        i = 1
        while i < len(intervals):
            # result[-1] automatically fetches the last interval in your result list
            prev = result[-1]
            prev_end = prev[1] # End is always at index 1
            current = intervals[i]
            
            # Simple check: If the new start time is less than or equal to the previous end time
            if current[0] <= prev_end:
                # Use max() so nested intervals like [2, 5] don't accidentally shrink [1, 10]
                prev[1] = max(prev[1], current[1])
                i += 1
            else:
                result.append(intervals[i])
                i += 1
                
        return result
