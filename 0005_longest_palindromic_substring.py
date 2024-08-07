# Given a string s, return the longest
# palindromic

# substring
#  in s.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(self, s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        if s == s[::-1]:
            return s

        n = len(s)
        start, end = 0, 0

        for i in range(n):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)

            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]


solution = Solution()

print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("bb"))
print(solution.longestPalindrome("cbbd"))
print(solution.longestPalindrome("babad"))
