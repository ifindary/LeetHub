class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1

        cnt = 1
        maxNums = nums[0]
        minNums = min(nums[1:])
        
        for i in range(0, len(nums)-1):
            # print(minNums, nums[i], min(nums[i+1:]))
            if minNums == nums[i]:
                minNums = min(nums[i+1:])
            
            maxNums = max(maxNums, nums[i])

            # print(maxNums, minNums)
            if maxNums <= minNums:
                return cnt
            else:
                cnt += 1

        return cnt