class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        num = 0
        for s in columnTitle[::-1]:
            ans += 26 ** num  * (ord(s) - ord("A") + 1)
            num += 1
        return ans
