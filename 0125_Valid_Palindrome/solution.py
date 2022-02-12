class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        for si, sj in zip(s, s[::-1]):
            if si == sj:
                pass
            else:
                return False
        return True
