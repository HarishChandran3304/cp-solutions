from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Default dicts don't throw KeyErrors no matter what.
        # If a key does not exist, it first initializes a key value pair using the default value parameter and then performs the requried operation
        hashmap = defaultdict(list)

        for word in strs:
            hashmap[tuple(sorted(word))].append(word)
                # Converting to tuple because keys have to be immutable
        
        return hashmap.values()