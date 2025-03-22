class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        idx, cnt = 0, 1
        ans = [0]*num_people
        
        while candies > 0:
            ans[idx] += min(candies, cnt)
            candies -= cnt
            cnt += 1

            idx = (idx+1) % num_people

        return ans