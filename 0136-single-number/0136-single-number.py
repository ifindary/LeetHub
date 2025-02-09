class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while True:
            tmp = 0

            for num in nums:
                tmp ^= num

            return tmp