def getWinner(arr: list[int], k: int) -> int:
    n=len(arr)-1
    count=1
    winner=arr[0]
    l=1
    for i in range(0,1):
            #print(arr,winner,count,i)
        if arr[1]>arr[0]:
            arr[1],arr[0]=arr[0],arr[1]
            count=0
        if arr[0]>=arr[1]:
            count+=1
        winner=arr[0]
        for r in range(n,(n//2)+1):
            if l==1:
                 arr[l],arr[r],arr[r-1]=arr[l+1],arr[r-1],arr[r]
                 print(arr)
            else:
                 arr[l],arr[r]=arr[l+1],arr[r-1]
            l+=1
            
                
    return 0
print(getWinner([2,1,3,5,4,6,7],2))

#     arr = [2,1,3,5,4,6,7], k = 2 Output: 5
# Round |       arr       | winner | win_count
#   1   | [2,1,3,5,4,6,7] | 2      | 1
#   2   | [2,3,5,4,6,7,1] | 3      | 1
#   3   | [3,5,4,6,7,1,2] | 5      | 1
#   4   | [5,4,6,7,1,2,3] | 5      | 2