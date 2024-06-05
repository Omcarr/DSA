class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans=0
        
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                
                if set(words[i]).intersection(set(words[j]))==set():
                    temp=len(words[j])*len(words[i])
                    ans=max(ans,temp)
                
        return ans
        