class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return 0 if citations[0] == 0 else 1

        citations.sort(reverse = True)
        possible_ans = []

        for i in range(len(citations)):
            if (i ) >= citations[i]:
                possible_ans.append(i)

        return len(citations) if not possible_ans else min(possible_ans)