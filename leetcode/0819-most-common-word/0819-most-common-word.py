class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.findall(r"\b[A-Za-z]+\b", paragraph)
        c = [x.lower() for x in paragraph]
        c = [x for x in c if x not in banned]
        f = {}
        for x in c:
            f[x] = f.get(x, 0) + 1
        f = dict(sorted(f.items(), key=lambda x: x[1], reverse=True))
        return list(f.keys())[0]