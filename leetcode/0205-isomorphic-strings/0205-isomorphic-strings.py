class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lst1 = []
        t_new = ''
        lst2 =[]

        for i in s:
            lst1.append(i)
        for j in t:
            lst2.append(j)

        my_dict = dict(zip(lst1, lst2))

        if len(set(my_dict.values())) == len(my_dict.values()):
            for i in s:
                t_new += my_dict[i]
            if t_new == t:
                return True
            else:
                return False

        else:
            return False
