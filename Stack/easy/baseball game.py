def calPoints(nums: list[str]) -> int:
        res=[]
        for i in range(len(nums)):
            if nums[i]=='+':
                res.append(sum(res[-2:]))
            elif nums[i]=='D':
                res.append(res[-1]*2)
            elif nums[i]=='C':
                res.pop()
            else:
                res.append(int(nums[i]))
        return sum(res[:])

print(calPoints(nums = ["5","2","C","D","+"]))