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
            i = stack.pop()
            res += mp[i].importance
            stack.extend(mp[i].subordinates)
        return res
        