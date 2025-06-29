class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        heap = nums[1:]
        heapq.heapify(heap)

        return nums[0] + heapq.heappop(heap) + heapq.heappop(heap)
        