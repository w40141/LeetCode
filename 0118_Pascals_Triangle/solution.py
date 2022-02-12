from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def comb(num_i: int, num_j: int) -> int:
            t_i, t_j = 1, 1
            for i, j in zip(range(num_i, 0, -1), range(num_j, 0, -1)):
                t_i *= i
                t_j *= j
            return t_i // t_j

        def make(num: int) -> List[int]:
            return [1] + [comb(num, i) for i in range(1, num + 1)]

        return [make(i) for i in range(numRows)]
