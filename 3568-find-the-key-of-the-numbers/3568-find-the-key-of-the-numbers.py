class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        strs = [str(num).rjust(4, '0') for num in nums]

        ans = ''.join(min(strs[0][i], strs[1][i], strs[2][i]) for i in range(4))

        return int(ans)