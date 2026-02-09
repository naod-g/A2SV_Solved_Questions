class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        freq = sorted(freq.items(), key = lambda x : x[1], reverse = True)
    
        for key, val in freq[:k]:
            res.append(key)
            
        return res
