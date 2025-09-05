class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return True if len(set(dict(Counter(arr)).values())) == len(set(arr)) else False