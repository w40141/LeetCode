class Solution:
    def romanToInt(self, s: str) -> int:
        mae = "M"
        ans = 0
        for r in s:
            if self.check(r) > self.check(mae):
                ans -= 2 * self.check(mae)
            ans += self.check(r)
            mae = r
        return ans

    def check(self, s: str) -> int:
        if s == "I":
            return 1
        elif s == "V":
            return 5
        elif s == "X":
            return 10
        elif s == "L":
            return 50
        elif s == "C":
            return 100
        elif s == "D":
            return 500
        else:
            return 1000
