# def maxArea(height: list[int]) -> int:
# #     height = [1,8,6,2,5,4,8,3,7]
# # Output: 49
#         r,lmax,rmax=len(height)-1,height[0],height[-1]
#         for i in range(0,len(height)-1):
#             lmax=max(lmax,height[i])
#             if height[r]>rmax and r>1:
#                   rmax=height[r]
#                   r-=1
#             print(lmax,rmax)
#         h=min(lmax,rmax)
#         l=lmax.in

# my approach 2
# def maxArea(height: list[int]) -> int:
#     n = len(height)-1
#     r=n
#     left=0
#     right=n
#     hright = height[-1]
#     hleft = height[0]
#     water=min(hright,hleft)*(n)
#     # goes from 1,n-1 becasue left should not become heigh[-1]
#     #similarly r cant become height[0] so r>=1
#     for l in range(1, n-1):
#         if r >= 1:
#             print(water)
#             if height[l] >= hleft:
#                 left = l
#                 hleft = height[l]
#             if height[r] >= hright:
#                 right = r
#                 hright = height[r]
#             length = min(hleft, hright)
#             breadth = right-left
#             print(hleft,hright)
#             if length*breadth>=water:
#                 r-=1
#                 water=length*breadth
#     return water


# optimalsolution
def maxArea(height):
        left = 0            
        right = len(height) - 1  
        maxWater = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            water = width * h
            maxWater = max(maxWater, water)
            # Move the pointers towards each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
print(maxArea([1,8,100,2,100,4,8,3,7]))
