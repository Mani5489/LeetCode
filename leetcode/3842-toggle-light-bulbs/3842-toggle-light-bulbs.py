class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        toggle = {}
        for i in bulbs:
            if i not in toggle:
                toggle[i] = 0
            v1 = toggle.get(i)
            if v1 == 0:
                toggle[i] = 1
            elif v1 == 1:
                toggle[i] = 0
        res = [x for x, y in toggle.items() if y == 1]
        return sorted(res)