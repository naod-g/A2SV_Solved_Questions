class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}

        for word in list1:
            if word in list2:
                mp[word] = list1.index(word) + list2.index(word)

        res = []
        mn = min(mp.values())


        for key, val in mp.items():
            if val == mn:
                res.append(key)

        return res

