class Solution:
    def longestPalindrome(self, s: str) -> str:
        return ""

    def judge_palindromic(self, s: str) -> bool:
        """docstring for sub_judge"""
        reversed_s = s[::-1]
        for i, j in zip(s, reversed_s):
            if i == j:
                continue
            else:
                return False
        return True

    def for_string(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            sub_s = s[i:]
            for j in range(len(sub_s)):
                sub_sub_s = sub_s[:-j]
