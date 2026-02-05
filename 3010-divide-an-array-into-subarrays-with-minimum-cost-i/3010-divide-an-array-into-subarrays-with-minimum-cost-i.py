class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        minSum = nums[0]
        nums.remove(minSum)
        nums.sort()

        for i in range(2):
            minSum += nums[i]

        return minSum