class Solution:
    def dps(self, s: str) -> str:
        if s is None or len(s) == 1:
            return s

        size = len(s)
        dps = [[False for _ in range(0, size)] for _ in range(0, size)]
        length, left = 1, 0
        print(dps)

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j] and (j - i < 3 or dps[i + 1][j - 1]):
                    dps[i][j] = True
                    if j - i + 1 > length:
                        length = j - i + 1
                        left = i
        return s[left:left + length]

    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 1:
            return s

        left, length, counter, size = 0, 1, 1, len(s)

        for i in range(0, size):
            l = i - 1
            r = i + 1

            # find duplicated char
            while r < size and s[i] == s[r]:
                r = r + 1
                counter = counter + 1

            # find left same right
            while l >= 0 and r < size and s[l] == s[r]:
                l = l - 1
                r = r + 1
                counter = counter + 2

            if counter > length:
                length = counter
                left = l + 1
            counter = 1

        return s[left:left + length]


if __name__ == "__main__":
    solution = Solution()
    res = solution.longestPalindrome("abcba")
    print(res)
