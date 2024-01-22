class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        #max sund initial window sum set to 0-k window
        maxS=window=sum(nums[:k])

        for i in range(1,len(nums)-k+1):
            #remove previous window element and add the next element
            window=window-nums[i-1]+nums[i+k-1]
            #the window with max sum at the end would be out our answer
            if window>maxS:
                maxS=window
                
        return maxS/k