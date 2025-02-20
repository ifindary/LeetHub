class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            tmp1 = num//10
            tmp2 = num//1000
            tmp3 = num//100000

            if (tmp1 > 0 and tmp1 < 10) or (tmp2 > 0 and tmp2 < 10) or (tmp3 == 1):
                ans += 1

        return ans