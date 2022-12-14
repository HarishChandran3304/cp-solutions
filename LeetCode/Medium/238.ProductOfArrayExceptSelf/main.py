from typing import List

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