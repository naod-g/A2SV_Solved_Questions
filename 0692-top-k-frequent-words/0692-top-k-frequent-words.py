class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = Counter(words)
        a = []

        for key,v in mp.items():
            a.append([key,v])
        a.sort(key = lambda x: (-x[1], x[0]))
        print(a)
        return [a[i][0] for i in range(k)]

        
