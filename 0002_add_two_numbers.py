# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pointer = head = ListNode()
        sum = 0

        while l1 or l2 or sum:
            pointer.next = ListNode()
            pointer = pointer.next

            sum += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            sum, pointer.val = divmod(sum, 10)

            l1 = l1.next if l1 else False
            l2 = l2.next if l2 else False

        return head.next


solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create second number: 465 (represented as 5 -> 6 -> 4)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Add the two numbers
result = solution.addTwoNumbers(l1, l2)

while result:
    print(result.val, end=" ")
    result = result.next
