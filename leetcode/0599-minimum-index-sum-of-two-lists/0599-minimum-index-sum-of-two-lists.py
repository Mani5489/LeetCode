class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minValue = float('inf')
        res = list(set(list1) & set(list2))
        results = []
        for i in res:
            index1 = list1.index(i)
            index2 = list2.index(i)
            if (index1 + index2) < minValue:
                minValue = (index1 + index2)
                results = [i]
            elif (index1 + index2) == minValue:
                results.append(i)
        return results
        