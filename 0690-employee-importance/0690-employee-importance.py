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
        mp = {e.id: [e.importance, e.subordinates] for e in employees}

        def dfs(id):
            nonlocal res
            res += mp[id][0]
            for sub_id in mp[id][1]:
                dfs(sub_id)
                    
        dfs(id)
        return res