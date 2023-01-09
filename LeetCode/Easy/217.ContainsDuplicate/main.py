from typing import List

class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False