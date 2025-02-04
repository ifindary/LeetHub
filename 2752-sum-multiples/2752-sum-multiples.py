class Solution:
    def sumOfMultiples(self, n: int) -> int:
        if n < 3:
            return 0
        
        nums = list(range(3, n+1))
        ans = 0

        for n in nums:
            if n%3 == 0 or n%5 == 0 or n%7 ==0:
                ans += n

        return ans