from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in nums:
                currlen = 1
                while True:
                    if n+1 in nums:
                        currlen += 1
                        n += 1
                    else:
                        longest = currlen if currlen > longest else longest
                        break
        
        return longest