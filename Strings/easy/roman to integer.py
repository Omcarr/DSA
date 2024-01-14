def romanToInt(s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(0,len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                number-=roman[s[i]]
            else:
                number+=roman[s[i]]
        return number+roman[s[-1]]

print(romanToInt("LVIIIV"))
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

#trick  here is that ROMAN number are alwayas represeted in descending order so if
#i<i+1 then its a special case and number i should be delted from tthe sum
#roman[s[-1]] has been added at the end separtely as  to avoid the out of range error at the
#case wehn i=len(s)-1 but i+1 will cause the error