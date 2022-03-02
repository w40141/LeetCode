import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = collections.Counter(s)
        t_dic = collections.Counter(t)
        return s_dic == t_dic
