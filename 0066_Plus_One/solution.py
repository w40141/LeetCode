class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = "".join(map(str, digits))
        digits_int = int(digits_str) + 1
        digits_str = str(digits_int)
        return list(map(int, digits_str))
