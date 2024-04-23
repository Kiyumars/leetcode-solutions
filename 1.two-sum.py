from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            if n not in h:
                h[n] = []
            h[n].append(i)
        for i, n in enumerate(nums):
            t = target - n
            if t in h:
                if t != n:
                    return [h[t][0], i]
                if len(h[t]) > 1:
                    return [h[t][1], i]
        return []