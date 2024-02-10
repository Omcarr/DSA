class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(ans):
            values=[]
            str1=''
            i=0
            while i<len(ans):
                freq=1
                while i+freq<len(ans) and ans[i+freq]==ans[i]:
                    freq+=1
                values.append([ans[i],freq])
                i+=freq

            for i in range(len(values)):
                    str1+=f'{values[i][1]}{values[i][0]}'
            return str1
        
        temp='1'
        while n!=1:
            n-=1
            temp=helper(temp)
        return temp
       

