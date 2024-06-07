class Solution:
    def convert(self, s: str, rows: int) -> str:
        res=[]
        for i in range(rows):
            res.append([])
        j=0
        while j<len(s):
            for i in range(rows):
                if j<len(s):
                    res[i].append(s[j])
                    # print(res)
                    j+=1
            for i in range(rows-2,0,-1):
                if j<len(s):
                    res[i].append(s[j])
                    # print(res)
                    j+=1
        ans=''
        for i in range(rows):
            ans+=''.join(res[i])
        return ans

        