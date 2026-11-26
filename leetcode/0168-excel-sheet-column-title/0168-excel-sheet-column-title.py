class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        str = 'ABCDEFGHIJKLMNOPQRSTVUWXYZ'
        list1 = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, rem = divmod(columnNumber, 26)
            list1.append(str[rem])
        # print(list1)
        rev = list1[::-1]
        return ''.join(rev)

        