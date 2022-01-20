from typing import List, Tuple


class Solution:
    def climbStairs(self, n: int) -> int:
        def k(n: int) -> int:
            num = 1
            for i in range(1, 1 + n):
                num *= i
            return num

        comb_list: List[Tuple[int, int]] = []
        for i in range(n // 2 + 1):
            comb_list.append((n - 2 * i, i))
        num = 0
        for c in comb_list:
            num += k(c[0] + c[1]) // (k(c[0]) * k(c[1]))
        return num
