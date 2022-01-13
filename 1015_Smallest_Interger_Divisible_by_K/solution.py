class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 5 == 0 or k % 2 == 0:
            return -1
        else:
            ans = 1
            now = 1
            while True:
                div = now % k
                if div == 0:
                    return ans
                else:
                    now = now * 10 + 1
                    ans += 1
