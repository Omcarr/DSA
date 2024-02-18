class Solution:
 def findPoisonedDuration(self,timeSeries: list[int], duration: int) -> int:
       freeze_time=0
       current_time=0
       for at in timeSeries:
            #if attcak time is grater than current itme simply add the duration to ft
            if at>current_time:
             freeze_time+=duration
             #if not ft will be dt-ct+at
            else:
             freeze_time+=duration-current_time+at
            current_time=at+duration
       return freeze_time            
 
#slightly better sol
class Solution:
    def findPoisonedDuration(self, t: list[int], d: int) -> int:
        ans=0
        f=0
        for i in t:
            if i<f:
                ans+=i-f
            ans+=d
            f=i+d

        return ans
           
