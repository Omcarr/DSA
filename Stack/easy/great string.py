class Solution:
    def makeGood(self, s: str) -> str:
        temp=[]
        n=len(s)
        while len(temp)!=n:
            for i in range(len(s)):
                if temp and s[i]!=temp[-1] and (s[i].upper()==temp[-1] or temp[-1].upper()==s[i]):
                    temp.pop()
                    n-=2
                else:
                    temp.append(s[i])
                  
        res=''
        for i in temp:
            res+=i
        return res
            
            

            
