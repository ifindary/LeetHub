class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while True:
            tmp = nums.pop()

            if not nums:
                return tmp

            if tmp in nums:
                nums.remove(tmp)
            else:
                return tmp

        