class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            tmp = nums.pop()

            if tmp in nums:
                nums.remove(tmp)
                nums.remove(tmp)
            else:
                return tmp