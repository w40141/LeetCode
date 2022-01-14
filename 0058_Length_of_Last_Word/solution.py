class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter = s.split()
        return len(letter[-1])
