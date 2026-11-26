class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        i = 0
        munits = 0
        while i < len(boxTypes) and truckSize > 0:
            box, units = boxTypes[i]
            if box > truckSize:
                box = truckSize
            munits += box * units
            i += 1
            truckSize -= box
        return munits

        