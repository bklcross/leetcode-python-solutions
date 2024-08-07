from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # edge case
        if len(p) > len(s): return []

        # initialize maps
        pMap, sMap = {}, {}
        
        # create maps
        for i in range(len(p)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            pMap[p[i]] = pMap.get(p[i], 0) + 1

        left = 0

        res = [0] if sMap == pMap else []

        # for each loop increase right pointer
        for right in range(len(p), len(s)):
            # update maps
            sMap[s[right]] = sMap.get(s[right], 0) + 1
            sMap[s[left]] -= 1

            # remove 0
            if sMap[s[left]] == 0:
                sMap.pop(s[left])

            left += 1

            # test
            if sMap == pMap:
                res.append(left)
        
        return res

solution = Solution()
print(solution.findAnagrams("cbaebabacd","abc"))
