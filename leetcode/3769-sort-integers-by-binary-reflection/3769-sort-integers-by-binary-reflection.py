class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        maps = []
        for i in nums:
            rev = int(str(bin(i)[2:])[::-1])
            maps.append((i, rev))
        maps = sorted(maps, key=lambda x: (x[1],x[0]))
        maps = [x[0] for x in maps]
        return maps