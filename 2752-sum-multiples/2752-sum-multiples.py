class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0

        for n in range(3, n+1):
            if n%3 == 0 or n%5 == 0 or n%7 ==0:
                ans += n

        return ans