class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # 1+3+5+... = k^2
        # 2+4+6+... = k(k+1)
        k1 = k2 = 1

        # case1: first row is red
        while True:
            redRow = (k1+1)//2
            blueRow = k1//2
            if (red - redRow**2) >= 0 and (blue - blueRow*(blueRow+1)) >= 0:
                k1 += 1
                continue
            else:
                break

        # case2: first row is blue
        while True:
            blueRow = (k2+1)//2
            redRow = k2//2
            if (blue - blueRow**2) >= 0 and (red - redRow*(redRow+1)) >= 0:
                k2 += 1
                continue
            else:
                break

        return max(k1, k2) - 1