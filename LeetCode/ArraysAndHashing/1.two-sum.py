# https://leetcode.com/problems/two-sum/
# Time: O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        
        for i, n in enumerate(nums):
            if target-n in hashmap:
                return [i, hashmap[target-n]]
            else:
                hashmap[n] = i