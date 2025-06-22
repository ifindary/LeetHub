class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var ans: [String] = []

        for i in 1...n {
            var tempStr = (i%3 == 0 ? "Fizz" : "") + (i%5 == 0 ? "Buzz" : "")

            ans.append(tempStr.isEmpty ? String(i) : tempStr)
        }
        
        return ans
    }
}