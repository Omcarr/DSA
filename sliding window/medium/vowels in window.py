#brute force
# def maxVowels(s: str, k: int) -> int:
#         V=['a', 'e', 'i', 'o','u']
#         res=0
#         v_cnt=0
#         for i in range(0,len(s)-k+1):
#             for i in s[i:i+k]:
#                 if i in V:
#                     v_cnt+=1
#             res=max(res,v_cnt)
#             v_cnt=0
#         return res

#optimal
def maxVowels(s: str, k: int) -> int:
        V=['a', 'e', 'i', 'o','u']
        v_cnt=0
        for i in s[:k]:
            if i in V:
                v_cnt+=1
        res=v_cnt
        
        for l in range(1,len(s)-k+1):
            if s[l-1] in V:
               v_cnt-=1
            if s[l+k-1] in V:
               v_cnt+=1
            res=max(v_cnt,res)

        return res
            


print(maxVowels(s = "abciiidef", k = 3))