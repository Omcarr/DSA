class Solution:
    def numSteps(self, s: str) -> int:
        carry=0
        res=0
        for i in range(len(s)-1,0,-1):
            digit=(int(s[i])+carry)%2
            if digit==0:
                res+=1
            else:
                res+=2
                carry=1
        return res+carry
