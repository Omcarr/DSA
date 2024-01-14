#brute forced but still accepted
def isHappy(n: int) -> bool:
    sum=n
    n=str(n)
    c=0
    while sum!=1 and c<25:
     n=str(sum)
     sum=0
     c+=1
     for i in n:
        sum+=pow(int(i),2)
    
    if c==25:
     return False
    return True

#optimalsolution
class Solution:
    def isHappy(self, n: int) -> bool:
        rep = []
        while(n != 1):
            if n in rep:
                return False
            rep.append(n)
            temp = 0
            for i in [int(x) for x in str(n)]:
                temp += (i*i)
            n = temp
        return True
print(isHappy(2))