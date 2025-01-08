class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumList = []
        temp = 0

        for i in range(0, len(nums)):
            temp += nums[i]
            sumList.append(temp)
        
        return sumList
