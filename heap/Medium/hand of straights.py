class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count={}
        for i in hand:
            count[i]=count.get(i,0)+1
        
        heap=list(count.keys())
        heapq.heapify(heap)

        while heap:
            i=heap[0]
            for j in range(i,i+groupSize):
                if not count.get(j,0):
                    return False
                count[j]-=1
                if count[j]==0:
                    if j!=heap[0]:
                        return False
                    heapq.heappop(heap)
        return True