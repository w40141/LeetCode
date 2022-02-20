from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_set = set()
        for i, n in enumerate(nums):
            if n in nums_set:
                return True

            nums_set.add(n)

            if len(nums_set) > k:
                nums_set.remove(nums[i-k])
        return False
