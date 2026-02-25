class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mp = defaultdict(int)
        mx = 0

        for right in range(len(s)):
            mp[s[right]] += 1

            while mp[s[right]] > 1:
                mp[s[left]] -= 1
                left += 1
            mx = max(mx, right - left + 1)

        return mx