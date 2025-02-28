class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumUnder10 = 0
        sumOver10 = 0

        for num in nums:
            if num < 10:
                sumUnder10 += num
            else:
                sumOver10 += num
        
        return sumUnder10 != sumOver10