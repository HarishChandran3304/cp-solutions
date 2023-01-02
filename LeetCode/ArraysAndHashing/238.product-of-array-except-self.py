from typing import List


# https://leetcode.com/problems/product-of-array-except-self/
# Time: O(n)
# Space: O(1)
# Technique: Postfix and Prefix

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = [None]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            a[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            a[i] *= postfix
            postfix *= nums[i]

        return a