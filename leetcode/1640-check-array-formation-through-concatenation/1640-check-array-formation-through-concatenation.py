class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        maps = {}
        for piece in pieces:
            maps[piece[0]] = piece
        res = []
        for i in arr:
            if i in maps.keys():
                res = res + maps[i]
        return res == arr