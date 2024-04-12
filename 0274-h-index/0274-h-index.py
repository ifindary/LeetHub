class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        citations.sort(reverse=True)
        
        for idx, citation in enumerate(citations):
            if citation >= idx+1:
                ans = idx+1
        
        return ans