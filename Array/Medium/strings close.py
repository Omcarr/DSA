def closeStrings(word1: str, word2: str) -> bool:
        c1={}
        c2={}
        i1,i2=[],[]
        for i in range(len(word1)):
            c1[word1[i]]=1+c1.get(word1[i],0)
        for i in range(len(word2)):
            c2[word2[i]]=1+c2.get(word2[i],0)
        
        if sorted(list(c1.keys()))!=sorted(list(c2.keys())):
             return False


        for key in c1.keys():
             i1.append(c1[key])
        for key in c2.keys():
             i2.append(c2[key])
        if sorted(i1)==sorted(i2):
             return True
        
        return False

print(closeStrings(word1 = "abc", word2 = "bca"))