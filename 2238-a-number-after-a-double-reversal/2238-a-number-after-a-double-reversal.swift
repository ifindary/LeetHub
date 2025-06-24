class Solution {
    func isSameAfterReversals(_ num: Int) -> Bool {
        return num == reserveNum(reserveNum(num))
    }

    func reserveNum(_ num: Int) -> Int {
        return Int(String(String(num).reversed()))!
    }
}