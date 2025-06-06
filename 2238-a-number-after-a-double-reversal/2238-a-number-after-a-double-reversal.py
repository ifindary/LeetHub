class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == self.reserveNum(self.reserveNum(num))

    def reserveNum(self, num: int) -> int:
        return int(str(num)[::-1])
    
