"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {e.id: e for e in employees}
        res = 0
        stack = [id]

        while stack:
            e = mp[stack.pop()]
            res += e.importance
            stack.extend(e.subordinates)
        return res
        