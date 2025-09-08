class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        strs = [str(num).rjust(4, '0') for num in nums]

        ans = 0

        for i in range(4):
            ans += min(int(strs[0][i]), int(strs[1][i]), int(strs[2][i])) * 10**(3-i)

        return ans