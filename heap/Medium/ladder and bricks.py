import heapq
#leetcode 1642
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        jumps = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(jumps, -diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(jumps)
        return len(heights) - 1
