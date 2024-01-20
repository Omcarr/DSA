class Solution:
    def reverseWords(self, s: str) -> str:
        s=' '.join(s.split())
        word=s.split(' ')
        res=''
        for i in range(len(word)-1,-1,-1):
            res+=word[i]
            if i!=0:
                res+=' '
        return res