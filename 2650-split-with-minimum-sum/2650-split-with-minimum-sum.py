class Solution:
    def splitNum(self, num: int) -> int:
        nums = list(str(num))
        nums.sort()

        nums1 = ''.join(nums[::2])
        nums2 = ''.join(nums[1::2])

        return int(nums1) + int(nums2)

        