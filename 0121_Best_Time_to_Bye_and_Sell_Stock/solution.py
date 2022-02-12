from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        num_max = -1
        num_min = 10000
        for i in prices:
            if i > num_max:
                num_max = i
            if num_min > i:
                ans = max(ans, num_max - num_min)
                num_max = i
                num_min = i
        return max(ans, num_max - num_min)
