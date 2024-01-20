
#MISREAD THE QUESTION, THE TRIPLET DIDNT NEED TO BE CONTINOUS

# def increasingTriplet(nums: list[int]) -> bool:
#         if len(nums)<3:
#             return False
#         for i in range(1,len(nums)-1):
#             print(nums[i-1],nums[i],nums[i+1])
#             if nums[i-1]<nums[i] and nums[i]<nums[i+1]:
#                 return True
#         for i in range(-1,1):
#             print(nums[i-1],nums[i],nums[i+1])
#             if nums[i-1]<nums[i] and nums[i]<nums[i+1]:
#                 return True
#         return False
    
# print(increasingTriplet([20,100,10,12,5,13]))


def increasingTriplet(nums: list[int]) -> bool:
        if len(nums)<3:
            return False
        first = float('inf')#positive infinty
        second = float('inf')
        for n in nums:
            if n<=first:
                first=n
                #first number
            elif n<=second:
                #if n>f, seconf number is present
                second=n
            elif n>second:
                #n>f>s exists here
                return True
        return False