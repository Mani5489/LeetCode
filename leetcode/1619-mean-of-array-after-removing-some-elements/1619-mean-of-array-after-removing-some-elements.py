class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        fp = (len(arr) / 100) * 5
        fp = round(fp)
        new = arr[fp:len(arr)-fp]
        return sum(new) / len(new)