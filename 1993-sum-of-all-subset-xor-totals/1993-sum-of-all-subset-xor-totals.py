class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            ans |= n

        return ans << (len(nums)-1)