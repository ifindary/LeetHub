class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0

        while True:
            if idx >= len(nums):
                return idx

            if nums[idx] < target:
                idx += 1
            else:
                return idx