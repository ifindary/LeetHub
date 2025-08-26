class Solution {
    func bestHand(_ ranks: [Int], _ suits: [Character]) -> String {
        var rankCnt : [Int:Int] = [:]
        var maxRanks : Int = 0
        var suitCnt : [Character:Int] = [:]
        var maxSuit = Set(suits).count

        for rank in ranks {
            rankCnt[rank, default: 0] += 1
        }
        maxRanks = rankCnt.values.max() ?? 0

        for suit in suits {
            suitCnt[suit, default: 0] += 1
        }
        maxSuit = suitCnt.values.max() ?? 0

        switch(maxRanks, maxSuit) {
            case(_, 5) : return "Flush"
            case(3...4, _) : return "Three of a Kind"
            case(2, _) : return "Pair"
            default : return "High Card"
        }
    }
}