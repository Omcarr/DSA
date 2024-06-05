def hammingWeight(n: int) -> int:
        count=0
        n=str(n)
        for i in n:
            if i=='1':
                count+=1
        return count

print(hammingWeight(11111111111111111111111111111101))