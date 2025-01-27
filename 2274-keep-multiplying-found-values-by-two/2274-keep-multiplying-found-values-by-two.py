class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original

        while ans in nums:
            ans *= 2
        
        return ans