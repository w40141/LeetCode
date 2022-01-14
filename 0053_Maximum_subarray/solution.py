class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10000000000000
        s = 0
        for i in range(len(nums)):
            s = max(s + nums[i], nums[i])
            ans = max(ans, s)
        return ans
