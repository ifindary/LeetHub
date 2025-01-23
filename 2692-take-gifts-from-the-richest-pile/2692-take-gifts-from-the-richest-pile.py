class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapGifts = [-x for x in gifts]        
        heapify(heapGifts)
        
        for _ in range(k):
            tmp = isqrt(-heappop(heapGifts))
            heappush(heapGifts, -tmp)

        return -sum(heapGifts)