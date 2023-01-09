from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        bucket = [[] for i in range(len(nums)+1)]
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n, count in freq.items():
            bucket[count].append(n)

        a = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                a.append(n)
                if len(a) == k:
                    return a