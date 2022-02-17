from typing import Dict, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d: Dict[int, int] = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        mv = 0
        mk = 0
        for k, v in d.items():
            if v > mv:
                mv = v
                mk = k
        return mk
