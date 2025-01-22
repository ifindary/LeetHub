class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        comsumedFuel = 0

        while mainTank > 0:
            if mainTank >= 5:
                mainTank -= 5
                comsumedFuel += 5

                if additionalTank > 0:
                    additionalTank -= 1
                    mainTank += 1
            else:
                comsumedFuel += mainTank
                mainTank = 0
        
        return comsumedFuel * 10
