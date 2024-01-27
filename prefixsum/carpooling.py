#Attempt one, couldnt figure out how to subtract passengers acocrding to current route

# def carPooling(trips: list[list[int]], capacity: int) -> bool:
#         st=trips[0][1]
#         end=trips[0][2]
#         passe=trips[0][0]
#         for i in range(1,len(trips)):
#             if trips[i][2]>end:
#                 passe-=passe ///wrong here
#             else:
#                 passe+=trips[i][0]
#                 end=max(end,trips[i][2])
#                 st=min(st,trips[i][1])
#             if passe>capacity:
#                 return False
#         return True

#optimal solution using sweep line/difference array algo
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        end=float('-inf')
        for i in range(len(trips)):
            end=max(end,trips[i][2])
        routes=[0]*(end+1)
        for i in range(len(trips)):
            routes[trips[i][1]]+=trips[i][0]
            routes[trips[i][2]]-=trips[i][0]

        if routes[0]<capacity:
           res=[routes[0]]
           for i in range(1,len(routes)):
                passengers=routes[i]+res[i-1]
                if passengers>capacity:
                    return False
                res.append(passengers)
           return True
        else:
            return False
