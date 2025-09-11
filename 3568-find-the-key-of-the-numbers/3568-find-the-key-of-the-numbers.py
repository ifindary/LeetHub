class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        strs = [str(num).rjust(4, '0') for num in nums]

        ans = ''.join(str(min(int(strs[0][i]), int(strs[1][i]), int(strs[2][i]))) for i in range(4))

        return int(ans)