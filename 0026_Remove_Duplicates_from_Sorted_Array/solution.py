class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        orig_len = len(nums)
        nums_set = set(nums)
        ans_len = len(nums_set)
        ans_li = list(nums_set) + 
