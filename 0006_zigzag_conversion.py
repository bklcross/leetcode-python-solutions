# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);


# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


class Solution(object):
    def convert(self, s, numRows):
        result = ""

        gap = numRows + (numRows - 2)
        target = 0
        diff = gap
        row = 0
        compliment = 0
        
        for i in range(len(s)):
            if compliment != gap:
                result += s[target]
            
            print("init: ", result)

            if compliment > 0 and len(s) > target + compliment:
                result += s[target + compliment]
                print("comp: ", result)

            target = target + diff + compliment

            compliment = gap - diff

            if target >= (len(s)):
                diff -= 2
                row += 1
                target = row
                compliment = 0


            print("row: ", row, " diff: ", diff, " target: ",target, " compliment: ",compliment, result)

            if len(s) <= len(result):
                print("end")
                break


        return result


solution = Solution()

print(solution.convert("PAYPALISHIRING", 4))
# print(solution.convert("PAYPALISHIRING", 4))
# print(solution.convert("PAYPALISHIRING", 5))

# PINALSIGYAHRPI
# PINALSIGYAHRPI




class Solution(object):
    def convert2(self, s, numRows):
        if numRows == 1:
            return s

        result = ""

        gap = numRows + (numRows - 2)
        target = 0
        diff = gap
        row = 0
        compliment = 0

        for i in range(len(s)):
            if compliment != gap:
                result += s[target]

            if compliment > 0 and len(s) > target + compliment:
                result += s[target + compliment]

            target = target + diff + compliment

            compliment = gap - diff

            if target >= (len(s)):
                diff -= 2
                row += 1
                target = row
                compliment = 0

            if len(s) <= len(result):
                print("end")
                break

        return result
