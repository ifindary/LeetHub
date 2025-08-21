class Solution(object):
    def bestHand(self, ranks, suits):
        setRanks = set(ranks)
        
        if len(set(suits)) == 1:
            return "Flush"
        elif len(setRanks) == 2 or len(setRanks) == 3:
            for rank in setRanks:
                if ranks.count(rank) >= 3:
                    return "Three of a Kind"
            return "Pair"
        elif len(setRanks) == 4:
            return "Pair"
        else:
            return "High Card"