class Solution:
    def countStudents(self, s: List[int], sandwiches: List[int]) -> int:
        students=[0,0]
        for i in s:
            students[i]+=1
        for i in sandwiches:
            if students[i]==0:
                return students[~i]
            else:
                students[i]-=1
        return 0
