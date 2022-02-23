class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        b = bin(n)
        print(b)
        one = b.count("1")
        if one == 1:
            return True
        else:
            return False
