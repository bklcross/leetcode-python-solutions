# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21
 
class Solution(object):
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1

        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            if result > (INT_MAX - pop) // 10:
                return 0
            
            result = result * 10 + pop
        
        return sign * result

    
solution = Solution()

print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
