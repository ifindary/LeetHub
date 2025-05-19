class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0

        for k in range(2, len(nums)):
            maxPrefix = nums[0]

            for j in range(1, k):
                ans = max(ans, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])

        return ans