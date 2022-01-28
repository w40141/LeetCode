from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m
        for i in range(m + n):
            print(i, nums1, nums2, end)
            if len(nums1) == 0:
                nums1[i] = nums2.pop(0)
                end += 1
            elif len(nums2) == 0:
                continue
            elif nums1[i] > nums2[0]:
                nums1.insert(i, nums2.pop(0))
                nums1.pop()
                end += 1
            elif nums1[i] == 0 and i == end:
                nums1[i] = nums2.pop(0)
                end += 1
            else:
                continue
