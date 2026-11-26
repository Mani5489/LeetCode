class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        maps = {i for i in allowed}
        for i in words:
            d = {j for j in i}
            if d <= maps:
                c += 1
        return c