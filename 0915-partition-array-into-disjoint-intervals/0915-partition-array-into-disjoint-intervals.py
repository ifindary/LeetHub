class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftArraySize = 1
        leftMaxNum = rightMaxNum = nums[0]

        for i in range(1, len(nums)):
            rightMaxNum = max(rightMaxNum, nums[i])

            if leftMaxNum > nums[i]:
                leftMaxNum = rightMaxNum
                leftArraySize = i + 1

        return leftArraySize