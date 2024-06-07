class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        V=['a', 'e', 'i', 'o','u']
        v_cnt=0
        for i in s[:k]:
            if i in V:
                v_cnt+=1
        res=v_cnt
        
        for l in range(k,len(s)):
            if s[l] in V:
               v_cnt+=1
            if s[l-k] in V:
               v_cnt-=1
            res=max(v_cnt,res)

        return res
        