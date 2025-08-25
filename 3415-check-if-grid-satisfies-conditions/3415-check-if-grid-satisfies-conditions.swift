class Solution {
    func satisfiesConditions(_ grid: [[Int]]) -> Bool {
        for i in 0..<grid.count {
            for j in 0..<grid[0].count {
                if (i+1 < grid.count && grid[i][j] != grid[i+1][j]) {
                    return false
                    }
                if (j+1 < grid[0].count && grid[i][j] == grid[i][j+1]) {
                    return false
                    }
            }
        }
        return true
    }
}