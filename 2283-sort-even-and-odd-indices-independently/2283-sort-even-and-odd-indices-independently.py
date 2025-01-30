class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddNums = []
        evenNums = []

        for i in range(len(nums)):
            if i%2 == 0:
                evenNums.append(nums[i])
            else:
                oddNums.append(nums[i])

        evenNums.sort()
        oddNums.sort(reverse=True)

        ans = []

        for i in range(len(nums)):
            if i%2 == 0:
                ans.append(evenNums[i//2])
            else:
                ans.append(oddNums[i//2])

        return ans