class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        runs = []
        j = 0
        for i in nums:
            j += i
            runs.append(j)
        # print(runs)
        coll = []
        for i in queries:
            c = 0
            for j in runs:
                if j <= i:
                    c += 1
            coll.append(c)
        return coll
        