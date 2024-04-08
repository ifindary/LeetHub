import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        A = math.sqrt(num)

        if A == int(math.sqrt(num)):
            return True
        else:
            return False