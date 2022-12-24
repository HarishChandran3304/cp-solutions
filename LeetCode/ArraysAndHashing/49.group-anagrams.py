# https://leetcode.com/problems/group-anagrams/
# Time: O(m*n), where m = avg length of a string and n = number of strings
# Space: O(n)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Default dicts don't throw KeyErrors no matter what.
        # If a key does not exist, it first initializes a key value pair using the default value parameter and then performs the requried operation
        hashmap = defaultdict(list)

        for word in strs:
            hashmap[tuple(sorted(word))].append(word)
                # Converting to tuple because keys have to immutable
        
        return hashmap.values()