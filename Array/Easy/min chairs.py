class Solution:
    def minimumChairs(self, s: str) -> int:
        chair=0
        res=0

        for i in s:
            if i =='E':    
                chair+=1
                res=max(chair,res)
            elif i=='L':
                chair-=1
        if res<0:
            return 0
        return res
        