class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        lis = sorted(list(set(s)))
        res = []
        var = ""

        for ch in lis:
            if count[ch] %2 == 1:
                var = ch
            for i in range(count[ch]//2):
                res.append(ch)

        temp = copy.deepcopy(res)
        if var != "":
            res.append(var)

        res.extend(temp[::-1])

        return "".join(res)




