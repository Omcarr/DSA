class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        if n==0:
            return 1
        elif x==0:
            return 0
        elif n<0:
            x=1/x
            n=-n
        
        while n:
            if n%2==0:
                x*=x
                n//=2
            else:
                res*=x
                n-=1
        return res