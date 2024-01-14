n=int(input())
#map used to map each list input to a int funtion. split to ignore the gaps
res=list(map(int, input().split()))
actualsum=n*(n+1)//2
sum=sum(res)
ans=actualsum-sum
print(ans)
