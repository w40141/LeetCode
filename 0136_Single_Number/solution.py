from typing import Dict, List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict: Dict[int, int] = {}
        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
        i = 0
        for k, v in num_dict.items():
            if v == 1:
                i = k
                break
            else:
                pass
        return i
