class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        order = 0
        cnt = 0
        prevValue = 1000

        dictNums = dict(zip(range(len(nums)), nums))
        sortedNums = sorted(dictNums.items(), key = lambda item:item[1])

        for i, v in sortedNums:
            if v > prevValue:
                cnt = 0
                ans[i] = order
            if v == prevValue:
                cnt += 1
                ans[i] = order - cnt

            order += 1
            prevValue = v

        return ans