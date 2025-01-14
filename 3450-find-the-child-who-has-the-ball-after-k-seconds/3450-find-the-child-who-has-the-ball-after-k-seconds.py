class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if k < n:
            return k

        time = 0
        order = 0
        direction = True # true : right, false: left

        while True:
            if time == k:
                return order
            
            time += 1

            if direction == True:
                if order == n-1:
                    direction = False
                    order -= 1
                else:
                    order += 1
            else:
                if order == 0:
                    direction = True
                    order += 1
                else:
                    order -= 1