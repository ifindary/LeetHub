class Solution {
    func distributeCandies(_ candies: Int, _ num_people: Int) -> [Int] {
        var idx: Int = 0
        var cnt: Int = 1
        var candies: Int = candies
        var ans = Array(repeating: 0, count: num_people)
        
        while candies > 0 {
            if candies < cnt {
                ans[idx] += candies
            }
            else {
                ans[idx] += cnt
            }

            candies -= cnt
            cnt += 1
            idx = idx+1

            if idx == num_people {
                idx = 0
            }
        }

        return ans
    }
}