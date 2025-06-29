class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        newNums = nums[1:]
        newNums.sort()

        return nums[0] + newNums[0] + newNums[1]
        