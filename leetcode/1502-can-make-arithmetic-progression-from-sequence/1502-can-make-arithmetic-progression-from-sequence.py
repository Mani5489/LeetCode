class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        r = sorted(arr, reverse=True) 
        p = r[0]
        ind1 = 1
        diffMax = []
        while ind1 < len(r):
            n = r[ind1]
            diffMax.append(p - n)
            p = n
            ind1 += 1
        e1 = diffMax[0]
        c = 0
        for i in range(0, len(diffMax)):
            e2 = diffMax[i]
            if e1 == e2:
                c += 1
        return True if len(diffMax) == c else False