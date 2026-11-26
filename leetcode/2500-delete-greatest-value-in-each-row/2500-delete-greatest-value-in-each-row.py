class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort(reverse=True)
        col = 0
        res = []
        while col < len(grid[0]):
            row = 0
            c = []
            while row < len(grid):
                c.append(grid[row][col])
                row += 1
            res.append(max(c))
            col += 1
        return sum(res)
        