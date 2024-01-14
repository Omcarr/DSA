def lengthOfLastWord(s: str) -> int:
        count=0
        s=s.strip()
        i=len(s)
        while i>0:
            if s[i-1]==' ':
                break
            count+=1
            i-=1
        return count
          

print(lengthOfLastWord("   fly me   to   the moon  "))
        