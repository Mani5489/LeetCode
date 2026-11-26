class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        freq = {}
        for i in trust:
            v = i[1]
            freq[v] = freq.get(v, 0) + 1
        print(freq)
        judge = list(set([x[1] for x in trust]))
        people = list(set([x[0] for x in trust]))
        value = []
        for i in judge:
            if i not in people:
                value.append(i)
        for i in value:
            if freq[i] == (n - 1):
                return i
        return -1