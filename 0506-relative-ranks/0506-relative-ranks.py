class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [0] * len(score)

        heap = [(-v, i) for i, v in enumerate(score)]
        heapq.heapify(heap)

        order = 0

        while heap:
            _, idx = heapq.heappop(heap)

            if order == 0:
                ans[idx] = "Gold Medal"
            elif order == 1:
                ans[idx] = "Silver Medal"
            elif order == 2:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(order+1)
                 
            order += 1

        return ans