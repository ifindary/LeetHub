class Solution(object):
    def bestHand(self, ranks, suits):
        maxRanksCnt = max(Counter(ranks).values())
        maxSuitsCnt = max(Counter(suits).values())

        if maxSuitsCnt == 5:
            return "Flush"
        elif maxRanksCnt == 3 or maxRanksCnt == 4:
            return "Three of a Kind"
        elif maxRanksCnt == 2:
            return "Pair"
        else:
            return "High Card"