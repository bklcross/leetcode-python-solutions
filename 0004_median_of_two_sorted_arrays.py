# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        length = len(merged)
        mid = length // 2

        if length % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0


solution = Solution()

nums1 = [1, 3]
nums2 = [2]

print(solution.findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]

print(solution.findMedianSortedArrays(nums1, nums2))
