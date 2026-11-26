class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char = [x.lower() for x in licensePlate if x.isalpha()]
        a = dict(Counter(char))
        # print(a)
        w = {}
        for word in words:
            wc = dict(Counter(word))
            result = {k: 0 if wc.get(k, 0) > a[k] else a[k] - wc.get(k, 0) for k in a}
            s = sum(x for x in result.values())
            w[word] = s
        w = dict(sorted(w.items(), key=lambda x: (x[1], len(x[0]))))
        # print(w)
        return list(w.keys())[0]