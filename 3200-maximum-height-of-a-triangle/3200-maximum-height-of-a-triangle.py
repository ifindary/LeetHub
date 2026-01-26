class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        red1 = red2 = red
        blue1 = blue2 = blue

        curRow1 = curRow2 = 1

        # case1: first row is red
        while red1 >= 0 and blue1 >= 0:
            if red1 >= curRow1:
                red1 -= curRow1
                curRow1 += 1
            else:
                break
            
            if blue1 >= curRow1:
                blue1 -= curRow1
                curRow1 += 1
            else:
                break

        # case2: first row is blue
        while red2 >= 0 and blue2 >= 0:
            if blue2 >= curRow2:
                blue2 -= curRow2
                curRow2 += 1
            else:
                break

            if red2 >= curRow2:
                red2 -= curRow2
                curRow2 += 1
            else:
                break
            
        return max(curRow1, curRow2) - 1