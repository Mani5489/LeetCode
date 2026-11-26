sys.set_int_max_str_digits(10000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string = "".join(map(str,num))
        sum = str(int(string)+k)
        return [int(i) for i in sum]




        