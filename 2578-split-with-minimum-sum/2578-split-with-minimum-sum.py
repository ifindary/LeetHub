class Solution:
    def splitNum(self, num: int) -> int:
        nums = list(map(int, str(num)))
        nums.sort()

        nums1 = ""
        nums2 = ""

        for i in range(0, len(nums), 2):
            nums1 += str(nums[i])

            if i+1 < len(nums):
                nums2 += str(nums[i+1])

        return int(nums1) + int(nums2)

        