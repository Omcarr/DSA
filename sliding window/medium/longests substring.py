class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        hash=set()
        pc=0
        for i in range(len(s)):
            while s[i] in hash:
                hash.remove(s[pc])
                pc+=1
            hash.add(s[i])
            res=max(res,i-pc+1)

        return res

            

            
