class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        end=meetings[0][1]
        cnt=meetings[0][0]-1
        for i,j in meetings:
            if i>end:
                cnt+=i-end-1
            end=max(end,j)
        if end<days:
            cnt+=days-end

        return cnt