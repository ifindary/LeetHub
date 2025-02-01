class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evenNums = [nums[i] for i in range(0, len(nums), 2)]
        oddNums = [nums[i] for i in range(1, len(nums), 2)]

        evenNums.sort()
        oddNums.sort(reverse=True)

        nums[::2] = evenNums
        nums[1::2] = oddNums

        return nums