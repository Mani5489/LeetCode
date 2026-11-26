class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        for i, j, k in zip(code, businessLine, isActive):
            if len(i) > 0 and all(ch.isalnum() or ch == "_" for ch in i) and j in ("electronics", "grocery", "pharmacy", "restaurant") and k:
                res.append((i, j))
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        return [code for code, _ in sorted(res, key=lambda x: (order[x[1]], x[0]))]
