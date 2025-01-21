class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [-1]*len(s)

        for i in range(len(s)):
            ans[indices[i]] = s[i]

        return "".join(ans)