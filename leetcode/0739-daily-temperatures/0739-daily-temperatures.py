class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mp = defaultdict(int)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                mp[temp] = (i-temp)

            stack.append(i)


        return [mp[t] for t in range(len(temperatures))]