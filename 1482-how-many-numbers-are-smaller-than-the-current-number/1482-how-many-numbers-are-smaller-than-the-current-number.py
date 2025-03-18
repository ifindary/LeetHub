class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dictNums = {}
        
        for idx, num in enumerate(sorted(nums)):
            if num not in dictNums:
                dictNums[num] = idx

        return [dictNums[num] for num in nums]