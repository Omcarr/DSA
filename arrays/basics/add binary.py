def addBinary(a: str, b: str) -> str:
    a=int(a,2)
    b=int(b,2)
    ans=a+b
    return bin(ans)[2:]

print(addBinary('1','11'))