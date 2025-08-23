class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """

        i = 0
        j = 0
        ans = True

        for i in range(len(grid)):
            if i+1 < len(grid):
                print(i, j)
                ans = ans and grid[i][j] == grid[i+1][j]

            for j in range(len(grid[0])):
                if j+1 < len(grid[0]) and i+1 < len(grid):
                    ans = ans and grid[i][j+1] == grid[i+1][j+1] and grid[i][j] != grid[i][j+1]
                elif j+1 < len(grid[0]):
                    print(i, j)
                    ans = ans and grid[i][j] != grid[i][j+1]

            if not ans:
                return ans

        return ans