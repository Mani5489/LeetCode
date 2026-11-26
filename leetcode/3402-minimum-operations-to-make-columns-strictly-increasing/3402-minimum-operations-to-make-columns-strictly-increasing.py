class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        clean = len(grid[0])
        c = 0
        op = 0
        while c < clean:
            c1 = [x[c] for x in grid]
            p = c1[0]
            for i in range(1, len(c1)):
                if c1[i] <= p:
                    d = p + 1
                    op += d - c1[i]
                    c1[i] = d
                p = c1[i]
            c += 1
        return op
        