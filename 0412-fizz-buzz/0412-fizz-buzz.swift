class Solution {
    func fizzBuzz(_ n: Int) -> [String] {
        var ans: [String] = []

        for i in 1...n {
            var tempStr: String = ""

            if i%3 == 0 {
                tempStr += "Fizz"
            }

            if i%5 == 0 {
                tempStr += "Buzz"
            }

            if tempStr == "" {
                tempStr = String(i)
            }
            
            ans.append(tempStr)
        }
        
        return ans
    }
}