class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        idx, cnt = 0, 1
        ans = [0]*num_people
        
        while candies > 0:
            if candies < cnt:
                ans[idx] += candies
            else:
                ans[idx] += cnt

            candies -= cnt
            cnt += 1
            idx = idx+1

            if idx == num_people:
                idx = 0

        return ans