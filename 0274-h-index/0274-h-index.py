class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        
        for idx, citation in enumerate(citations):
            if citation >= idx+1:
                ans = idx+1
        
        return ans