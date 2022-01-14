import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else bisect.bisect(nums, target)
