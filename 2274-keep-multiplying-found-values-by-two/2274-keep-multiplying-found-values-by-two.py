class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        setNums = set(nums)
        ans = original

        while ans in setNums:
            ans *= 2
        
        return ans