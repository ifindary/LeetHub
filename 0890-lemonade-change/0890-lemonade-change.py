class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5:
            return False
        
        wallet = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                wallet[5] += 1
            else:
                if wallet[5] < 1:
                    return False
            
            if bill == 10:
                if wallet[5] < 1:
                    return False
                else:
                    wallet[5] -= 1
                    wallet[10] += 1
            elif bill == 20:
                if wallet[10]*10 + wallet[5]*5 < 15:
                    return False
                elif wallet[10] >= 1 and wallet[5] >= 1:
                    wallet[10] -= 1
                    wallet[5] -= 1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        
        return True
