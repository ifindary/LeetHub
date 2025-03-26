class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meetingDays = []
        cnt = 0

        for meeting in meetings:
            if not meetingDays or meetingDays[-1][1] < meeting[0]:
                meetingDays.append(meeting)
            else:
                meetingDays[-1][1] = max(meetingDays[-1][1], meeting[1])
        
        for s, e in meetingDays:
            cnt += (e - s + 1)

        return days - cnt