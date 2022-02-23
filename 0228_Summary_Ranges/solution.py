from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = []
        first = nums[0]
        now = nums[0]
        for n in nums[1:]:
            if n == now + 1:
                now = n
            else:
                if first == now:
                    ans.append(str(now))
                else:
                    ans.append(f"{first}->{now}")
                first = n
                now = n
        else:
            if first == now:
                ans.append(str(now))
            else:
                ans.append(f"{first}->{now}")
        return ans
