
#incomplete

import heapq
def totalCost( costs: list[int], k: int, c: int) -> int:
        cost=0
        costs=[[costs[i],i] for i in range(len(costs))]
        print(costs)
        while k>0:
            if c<len(costs):
                tmp1=costs[:c]
                tmp2=costs[-c:]
                heapq.heapify(tmp1)
                heapq.heapify(tmp2)
                if tmp1[0][0]>tmp2[0][0]:
                   t=heapq.heappop(tmp2)
                else:
                   t=heapq.heappop(tmp1)
                print(t)
                
                cost+=t[0]
                #costs.pop(t[])

            else:
              heapq.heapify(costs)
              t=heapq.heappop(costs)
              cost+=t
            k-=1

        return cost

print(totalCost([50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58],7,12))