class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        str1 = str(num1).rjust(4, '0')
        str2 = str(num2).rjust(4, '0')
        str3 = str(num3).rjust(4, '0')

        ans = 0

        for i in range(4):
            ans += min(int(str1[i]), int(str2[i]), int(str3[i])) * 10**(3-i)

        return ans