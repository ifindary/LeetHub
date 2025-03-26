class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prevE = 0

        for s, e in meetings:
            s = max(s, prevE + 1)
            period = e - s + 1
            days -= max(period, 0)
            prevE = max(prevE, e)

        return days