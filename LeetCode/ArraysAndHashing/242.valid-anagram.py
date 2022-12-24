# https://leetcode.com/problems/valid-anagram
# Time: O(nlogn)
# Space: O(1)

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)