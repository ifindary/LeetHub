class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        comsumedFuel = 0

        while mainTank >= 5 and additionalTank > 0:
            mainTank -= 4
            comsumedFuel += 5
            additionalTank -= 1
        
        comsumedFuel += mainTank

        return comsumedFuel * 10
