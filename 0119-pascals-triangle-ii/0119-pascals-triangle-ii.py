class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 1
        # 1 1 1
        # 2 1 2 1
        # 3 1 3 3 1
        # 4 1 4 6 4 1
        # 5 1 5 10 10 5 1
        # 6 1 6 15 20 15 6 1
        # 7 1 7 21 35 35 21 7 1

        newRow1 = [1]
        newRow2 = [1]
        now = 1
        curIndex = 1

        while curIndex <= rowIndex:
            if now == 1:
                newRow2 = [1] * (curIndex + 1)

                for i in range(1, len(newRow1)):
                    newRow2[i] = newRow1[i-1] + newRow1[i]

                now = 2
                curIndex += 1
            else:
                newRow1 = [1] * (curIndex + 1)

                for i in range(1, len(newRow2)):
                    newRow1[i] = newRow2[i-1] + newRow2[i]

                now = 1
                curIndex += 1

        if now == 1:
            return newRow1
        else:
            return newRow2