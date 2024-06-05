def isValid(s: str) -> bool:
        signs=[]
        v={'[':']','(':')','{':'}'}

        for i in range(len(s)):
            if s[i] in v.keys():
               signs.append(s[i])
            elif not signs or s[i]!=v.get(signs[-1],0):
                return False
            else:
              signs.pop()

        return not signs
                
print(isValid(s="(])"))