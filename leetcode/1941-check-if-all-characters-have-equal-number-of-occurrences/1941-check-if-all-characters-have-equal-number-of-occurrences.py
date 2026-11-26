class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        v = max(Counter(s).values())
        values = Counter(s).values()
        return all(v == i for i in values)