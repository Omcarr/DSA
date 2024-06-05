import heapq


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    dist = []
    for i in range(len(points)):
        t = pow(points[i][0], 2)+pow(points[i][1], 2)
        dist.append([t,points[i]])

    heapq.heapify(dist)
    ans = []
    for _ in range(k):
        if dist:
            l = heapq.heappop(dist)
            if l[1] not in ans:
                ans.append(l[1])
    return ans


print(kClosest(points=[[3,3],[5,-1],[-2,4]], k=2))
