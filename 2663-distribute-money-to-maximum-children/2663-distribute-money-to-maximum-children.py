class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        if money == children * 8:
            return children
        if money > children * 8:
            return children - 1

        ans = 0
        money -= children
        
        while True:
            if money >= 7 and ans < children:
                money -= 7
                ans += 1
            elif money == 3 and ans >= children - 1:
                money = 0
                ans -= 1
                break
            else:
                money = 0
                break

        return ans