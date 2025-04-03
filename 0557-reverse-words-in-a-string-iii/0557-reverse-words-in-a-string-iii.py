class Solution:
    def reverseWords(self, s: str) -> str:
        newS = list(s.split(' '))
        ans = []

        for ns in newS:
            ns = list(ns)
            ans.append(''.join(ns[::-1]))

        return ' '.join(ans)