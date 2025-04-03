class Solution:
    def reverseWords(self, s: str) -> str:
        newS = s.split()
        ans = ''

        for n in newS:
            ans += n[::-1]
            ans += ' '

        return ans[:-1]