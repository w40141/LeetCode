class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int("0b" + a, 0)
        b_int = int("0b" + b, 0)
        ans_int = a_int + b_int
        return bin(ans_int)[2:]
