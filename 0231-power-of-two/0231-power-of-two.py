class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        a = bin(n)
        b = bin(n-1)

        result = int(a, 2) & int(b, 2)

        if result == 0:
            return True
        else:
            return False