class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        mini = float('inf')
        for i in range(len(landStartTime)):
            ls = landStartTime[i]
            ld = landDuration[i]
            for j in range(len(waterStartTime)):
                ws = waterStartTime[j]
                wd = waterDuration[j]
                lt = ls + ld
                wt = ws + wd
                min1 = (max(lt, ws)) + wd
                min2 = (max(wt, ls)) + ld
                res = min(min1, min2)
                mini = min(mini, res)
        return mini