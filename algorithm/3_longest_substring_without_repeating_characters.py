class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res, dict = 0, 0, {}
        for i in range(0, len(s)):
            if s[i] in dict and dict[s[i]] >= left:
                left = dict[s[i]] + 1
            res = res if (i - left + 1) < res else i - left + 1
            dict[s[i]] = i
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "abba"
    res = solution.lengthOfLongestSubstring(s)
    print(res)
