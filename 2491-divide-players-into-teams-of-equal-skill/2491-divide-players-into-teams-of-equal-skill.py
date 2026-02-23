class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0
        i = 0
        j = len(skill) - 1

        total = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] == total:
                res += (skill[i] * skill[j])
                i += 1
                j -= 1
            else:
                return -1
        return res