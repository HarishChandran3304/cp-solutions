# https://leetcode.com/problems/contains-duplicate/
# Time: O(n)
# Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False