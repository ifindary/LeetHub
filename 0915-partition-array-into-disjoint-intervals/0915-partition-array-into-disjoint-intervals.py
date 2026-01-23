class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1

        cnt = 1
        maxNum = nums[0]
        minNums = [0]*len(nums)
        minNums[-1] = nums[-1]
        
        for i in range(len(nums)-2, -1, -1):
            minNums[i] = min(nums[i], minNums[i+1])
        
        for i in range(0, len(nums)-1):            
            maxNum = max(maxNum, nums[i])

            if maxNum <= minNums[i+1]:
                return cnt
            else:
                cnt += 1

        return cnt