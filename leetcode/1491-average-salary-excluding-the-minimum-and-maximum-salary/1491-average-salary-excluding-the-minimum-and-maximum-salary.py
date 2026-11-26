class Solution:
    def average(self, salary: List[int]) -> float:
        salary.pop(salary.index(min(salary)))
        salary.pop(salary.index(max(salary)))
        if salary is None:
            return 0
        else:
            return sum(salary) / len(salary)