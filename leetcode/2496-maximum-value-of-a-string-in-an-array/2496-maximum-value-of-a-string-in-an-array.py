class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxs = 0
        for i in strs:
            try:
                int(i)
                is_true = True
            except ValueError:
                is_true = False
            if is_true:
                # print(int(i))
                if int(i) > maxs:
                    maxs = int(i)
            else:
                if len(i) > maxs:
                    maxs = len(i)
        return maxs


        