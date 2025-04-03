class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(newS[::-1] for newS in s.split())