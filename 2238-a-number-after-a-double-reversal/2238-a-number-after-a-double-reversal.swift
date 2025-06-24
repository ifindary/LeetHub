class Solution {
    func isSameAfterReversals(_ num: Int) -> Bool {
        return num == self.reserveNum(self.reserveNum(num))
    }

    func reserveNum(_ num: Int) -> Int {
        return Int(String(String(num).reversed()))!
    }
}