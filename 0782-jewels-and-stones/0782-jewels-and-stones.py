class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = list(jewels)
        stone = list(stones)

        cnt = 0

        for i in stone:
            if i in jewel:
                cnt += 1
        
        return cnt
