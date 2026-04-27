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
        mp = {e.id: [e.importance, e.subordinates] for e in employees}

        def dfs(id):
            return mp[id][0] + sum(dfs(sub_id) for sub_id in mp[id][1])
            
        return dfs(id)