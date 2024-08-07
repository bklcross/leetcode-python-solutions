from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        # check edge case p > s
        if len(p) > len(s): return result

        # initialize maps
        sCount = {}
        pCount = {}

        # prepare two maps - get first sets
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        print(pCount)
        print(sCount)

        # set up reading frame pointer
        left = 0

        # initial window check - check edge case p == s
        result = [0] if sCount == pCount else []
        
        # each loop shifts right by 1
        for right in range(len(p), len(s)):
            print("char", s[right])

            sCount[s[right]] = sCount.get(s[right], 0) + 1  # add to last character
            sCount[s[left]] -= 1  # remove from first character

            # remove from map
            if sCount[s[left]] == 0:
                sCount.pop(s[left])

            # shift left
            left += 1

            if (sCount == pCount):
                result.append(left)

            print(pCount)
            print(sCount)

        return result

solution = Solution()

print(solution.findAnagrams("cbaebabacd","abc"))
print(solution.findAnagrams("abab","ab"))
