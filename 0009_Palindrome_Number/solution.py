class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            if x % 10 == 0:
                return False
            ans = 0
            x_copied = x
            while x:
                tmp = x % 10
                ans = ans * 10 + tmp
                x //= 10
            if x_copied == ans:
                return True
            else:
                return False
