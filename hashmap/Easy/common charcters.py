class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count=defaultdict(int)
        res=[]
        for i in words[0]:
            count[i]+=1  
        
        for i in range(1,len(words)): 
            temp=defaultdict(int)
            for j in words[i]:
                temp[j]+=1
            for key in count.keys():
                    count[key]=min(count[key],temp[key])
                    
        for key in count.keys():
            while count[key]:
                res.append(key)
                count[key]-=1
        return res

        