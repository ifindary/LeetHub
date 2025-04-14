class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [0] * len(score)

        dictScore = dict(enumerate(score))
        sortDictScore= dict(sorted(dictScore.items(), key=lambda x: x[1], reverse=True))

        order = 1

        for key, value in sortDictScore.items():
            if order == 1:
                ans[key] = "Gold Medal"
            elif order == 2:
                ans[key] = "Silver Medal"
            elif order == 3:
                ans[key] = "Bronze Medal"
            else:
                ans[key] = str(order)
                 
            order += 1

        return ans