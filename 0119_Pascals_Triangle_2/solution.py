from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def comb(num_i: int, num_j: int) -> int:
            t_i, t_j = 1, 1
            for i, j in zip(range(num_i, 0, -1), range(num_j, 0, -1)):
                t_i *= i
                t_j *= j
            return t_i // t_j

        return [1] + [comb(rowIndex, i) for i in range(1, rowIndex + 1)]
