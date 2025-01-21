class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [-1]*len(s)

        for i, v in enumerate(indices):
            ans[v] = s[i]

        return "".join(ans)