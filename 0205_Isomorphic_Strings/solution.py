from typing import Dict, List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_d: Dict[str, List[int]] = {}
        t_d: Dict[str, List[int]] = {}
        for i, si in enumerate(s):
            if si in s_d:
                s_d[si].append(i)
            else:
                s_d[si] = [i]
        for i, ti in enumerate(t):
            if ti in t_d:
                t_d[ti].append(i)
            else:
                t_d[ti] = [i]
        for a, b in zip(s_d.values(), t_d.values()):
            if a == b:
                pass
            else:
                return False
        return True
