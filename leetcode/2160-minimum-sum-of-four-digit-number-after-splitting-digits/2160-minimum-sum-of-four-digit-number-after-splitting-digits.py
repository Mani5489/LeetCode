class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(list(map(int, str(num))))
        p = []
        for i, j in zip(nums[0:2], nums[2:4]):
            p.append(str(i) + str(j))
        return reduce(lambda x, y: int(x) + int(y), map(int, p))
        