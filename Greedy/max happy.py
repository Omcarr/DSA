class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        res=0
        h.sort(reverse=True)
        for i in range(k):
            if h[i]-i>0:
                res+=h[i]-i
        return res
            