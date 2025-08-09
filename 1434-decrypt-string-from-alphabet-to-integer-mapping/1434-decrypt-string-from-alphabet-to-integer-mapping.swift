class Solution {
    func freqAlphabets(_ s: String) -> String {
        var ans: [Character] = []
        var i = 0
        var chars = Array(s)

        while (i < chars.count) {
            if (i+2 < chars.count && chars[i+2] == "#") {
                let num1 = Int(String(chars[i]) + String(chars[i+1]))!
                let num2 = UnicodeScalar(num1 + 96)!
                ans.append(Character(num2))
                i += 3
            }
            else {
                let num1 = Int(String(chars[i]))!
                let num2 = UnicodeScalar(num1+96)!
                ans.append(Character(num2))
                i += 1
            }
        }

        return String(ans)
    }
}