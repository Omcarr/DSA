class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        #brut forced 
        res = []
        for i in range(len(arr)):
            j = i+1
            while j < len(arr):
                res.append(arr[i]/arr[j])
                j += 1         
        res.sort()
        for i in range(len(arr)):
            j = i+1
            while j < len(arr):
                if arr[i]/arr[j] == res[k-1]:
                    return [arr[i], arr[j]]
                j += 1 