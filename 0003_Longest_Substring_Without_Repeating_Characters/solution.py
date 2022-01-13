class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def helper(string: str) -> int:
            tmp_string = ''
            ans = 0
            for s in string:
                if s in tmp_string:
                    tmp_string = tmp_string[tmp_string.index(s) + 1:] + s
                else:
                    tmp_string += s
                if len(tmp_string) > ans:
                    ans = len(tmp_string)
            return ans
        return helper(s)
