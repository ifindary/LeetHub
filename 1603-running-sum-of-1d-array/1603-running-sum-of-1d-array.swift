class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        var ans: [Int] = []
        var tmp = 0

        for num in nums {
            ans.append(tmp + num)
            tmp += num
        }

        return ans
    }
}