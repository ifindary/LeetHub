class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0

        for money in accounts:
            if sum(money) >= ans:
                ans = sum(money)

        return ans