from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        ca = Counter(a)
        cb = Counter(b)
        
        for x in cb:
            if cb[x] > ca[x]:
                return False
        return True
    
