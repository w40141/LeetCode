from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans: int = max(map(sum, accounts))
        return ans
