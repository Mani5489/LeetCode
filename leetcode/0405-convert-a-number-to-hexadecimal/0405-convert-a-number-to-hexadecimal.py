class Solution:
    def toHex(self, num: int) -> str:
        maps = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
                6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
                11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        res = []
        if num > 0:
            while num > 0:
                val = num % 16
                res.append(maps.get(val, 0))
                num = num // 16
            return ''.join(map(str, res))[::-1].lower()
        elif num < 0:
            return f"{(num & 0xFFFFFFFF):08x}"
        else:
            return '0'
        