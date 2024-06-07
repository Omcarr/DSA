class Solution:
    def compress(self, c: List[str]) -> int:
        ans=0
        i=0
        while i<len(c):
            letter=c[i]
            cnt=0
            while i<len(c) and c[i]==letter:
                cnt+=1
                i+=1
            c[ans]=letter
            ans+=1
            if cnt>1:
                for r in str(cnt):
                    c[ans]=r
                    ans+=1
        return ans

            



       