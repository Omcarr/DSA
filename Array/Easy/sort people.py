class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res={}
        for i in range(0,len(names)):
            res[heights[i]]=names[i]
        
        heights=sorted(heights)
        n=[]
        for i in range(len(heights)-1,-1,-1):
            n.append(res[heights[i]])
        
        return n
