class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def b_search(self, nums, target, now):
            n = int(len(nums) / 2)
            if len(nums) == 0:
                print('NOT FOUND')
                return -1
            if nums[n] == target:
                print('FOUND')
                return now
            elif nums[n] < target:
                print('Big')
                nums = nums[n:]
                now += int(len(nums) / 2)
                return self.b_search(nums, target, now)
            else:
                print('SMALL')
                nums = nums[:n]
                now -= int(len(nums) / 2)
                return self.b_search(nums, target, now)

        return self.b_search(nums, target, int(len(nums) / 2))
