class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(n, cntOpen, cntClose, curStr):
            if cntOpen < n:
                dfs(n, cntOpen + 1, cntClose, curStr+"(")

            if cntClose < cntOpen:
                dfs(n, cntOpen, cntClose+1, curStr+")")

            if cntOpen == n and cntClose == n:
                ans.append(curStr)
                return

        dfs(n, 0, 0, '')

        return ans

