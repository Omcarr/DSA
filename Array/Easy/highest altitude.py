def largestAltitude(gain: list[int]) -> int:
    for i in range(1,len(gain)):
        gain[i]=gain[i]+gain[i-1]
    gain=sorted(gain)[-1]
    if gain>0:
        return gain
    else:
        return 0
    
print(largestAltitude([-4,-3,-2,-1,4,3,2]))