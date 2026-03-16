class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit = 0
        freq = Counter(answers)

        for r, c in freq.items():
            if r == 0:
                rabbit += c
                continue

            cycle = max(1, ceil(c / (r+1)))
            rabbit += cycle * (r+1)
            
        return rabbit