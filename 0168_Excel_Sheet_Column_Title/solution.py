class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber != 0:
            n = columnNumber % 26
            if n == 0:
                n = 26
            s = chr(n + ord("A") - 1) + s
            columnNumber //= 26
            if n == 26:
                columnNumber -= 1
        return s
