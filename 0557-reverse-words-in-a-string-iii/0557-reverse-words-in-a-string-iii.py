class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []

        for newS in s.split():
            ans.append(''.join(newS[::-1]))

        return ' '.join(ans)