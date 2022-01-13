class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        first: str = strs[0]
        common: str = ""
        test: str = ""
        for f in first:
            test += f
            for si in strs[1:]:
                if not si.startswith(test):
                    return common
            common = test
        return common
