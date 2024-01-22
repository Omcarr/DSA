import math
AB=int(input())
BC=int(input())
AC= math.sqrt(pow(AB, 2) + pow(BC, 2))
MC=AC//2
x=math.asin(BC/AC)
x=math.degrees(x)
res=90-x

print(round(res))