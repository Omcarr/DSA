def plusOne(digits):
        num=1
        n=len(digits)-1
        for i in range(0,len(digits)):
            num+=digits[i]*pow(10,n)
            n-=1
        
        num=str(num)
        digits=[0]*len(num)
        for i in range(len(num)):
              digits[i]=int(num[i])
              
        return digits

print(plusOne([9,9,9]))