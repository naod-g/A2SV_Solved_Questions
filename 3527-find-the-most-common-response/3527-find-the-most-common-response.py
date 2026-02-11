class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        new = []
        mp = defaultdict(int)
        
        #discarding reapting responses
        for i in range(len(responses)):
            new.append(list(set(responses[i])))

        #building  dict from  non-repeating dics
        for i in range(len(new)):
            for response in new[i]:
                mp[response] += 1
        print(mp)
        print()
        #sorting the dict with occurance then with lexicographically
        mp = sorted(list(mp.items()), key = lambda x : (-x[1], x[0]))

        return mp[0][0]