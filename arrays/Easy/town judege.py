class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_cnt=[0]*n
        trusted_cnt=[0]*n
        for a,b in trust:
            trust_cnt[a-1]+=1
            trusted_cnt[b-1]+=1
        for i in range(0,n):
            if trust_cnt[i]==0:
                if trusted_cnt[i]==n-1:
                    return i+1
        return -1
            
            


