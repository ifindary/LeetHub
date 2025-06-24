class Solution {
    func isSameAfterReversals(_ num: Int) -> Bool {
        return num == reserveNum(reserveNum(num))
    }

    func reserveNum(_ num: Int) -> Int {
        let reserveStr = String(String(num).reversed())
        return Int(reserveStr)!
    }
}