class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(n: int) -> int:
            ans = 0
            while True:
                t = n % 10
                ans += t ** 2
                n //= 10
                if n == 0:
                    break
            return ans

        seen = set()
        while True:
            ans = calc(n)
            if ans == 1:
                return True
            elif ans in seen:
                return False
            else:
                seen.add(ans)
                n = ans
