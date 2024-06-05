class Solution:
   def sortTheStudents(self,score: list[list[int]], k: int) -> list[list[int]]:
        k_score=[]
        res={}

        for i in range(0,len(score)):
            k_score.append(score[i][k])
            res[score[i][k]]=i

        k_score=sorted(k_score,reverse=True)
        ans=[]
        
        for i in k_score:
              ans.append(score[res[i]])
        
        return ans


        