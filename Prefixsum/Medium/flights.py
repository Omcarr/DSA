#TLE O(n2)
# def corpFlightBookings(bookings: list[list[int]], n: int) -> list[int]:
#     flights=[0]*n
#     for i in range(len(bookings)):
#         for j in range(bookings[i][0]-1,bookings[i][1]):
#             flights[j]+=bookings[i][2]
#     return flights

#difference array algo/Prefix sum algo
class Solution:
    def corpFlightBookings(self, b: list[list[int]], n: int) -> list[int]:
        f=[0]*(n+1)
        for i in range(len(b)):
            f[b[i][0]-1]+=b[i][2]
            f[b[i][1]]-=b[i][2]
        res=[f[0]]
        for i in range(1,len(f)-1):
            res.append(res[i-1]+f[i])
        return res

