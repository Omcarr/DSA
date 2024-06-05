class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans=0
        people.sort()
        i,j=0,len(people)-1
        while i<=j:
            load=people[i]+people[j]
            if load<=limit:
                i+=1
                j-=1
            else:
                j-=1
        
            ans+=1
        return ans
            