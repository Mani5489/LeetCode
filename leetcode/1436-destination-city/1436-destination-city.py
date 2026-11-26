class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        source = set()
        for i in paths:
            s = i[0]
            source.add(s)
        for i in paths:
            d = i[1]
            if d not in source:
                return d
        return '' 