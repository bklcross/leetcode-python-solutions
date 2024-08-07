# Given a string s, find the length of the longest
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {}
        left = 0
        max_length = 0

        for right, current in enumerate(s):
            if current in char_index and char_index[current] >= left:
                left = char_index[current] + 1
            char_index[current] = right
            max_length = max(max_length, right - left + 1)

        return max_length


# Example usage:
solution = Solution()
s = "abba"
print(
    "Length of the longest substring without repeating characters:",
    solution.lengthOfLongestSubstring(s),
)  # Output: 3
