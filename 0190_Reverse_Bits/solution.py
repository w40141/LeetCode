class Solution:
    def reverseBits(self, n: int) -> int:
        s = '{:032}'.format(bin(n)[::-1][:-2])
        b = '0b' + s
        return int(b, 2)
