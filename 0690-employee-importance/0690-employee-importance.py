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
        res = 0

        def dfs(id):
            nonlocal res
            for e in employees:
                if e.id == id:
                    res += (e.importance)

                    for sub_id in e.subordinates:
                        dfs(sub_id)
                    break
        dfs(id)
        return res