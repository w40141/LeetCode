class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if h_len == n_len and haystack == needle:
            return 0
        for i in range(0, h_len):
            if haystack[i: i + n_len] == needle:
                return i
        return -1
