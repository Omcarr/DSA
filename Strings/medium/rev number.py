class Solution:
    def reverse(self, x: int) -> int:
     x=str(x)
     if x[0]!='-':
      res=''.join(x[i] for i in range(len(x)-1,-1,-1))
     else:
      res='-'
      res+=''.join(x[i] for i in range(len(x)-1,0,-1))
     res=int(res)
     if res>(pow(2,31)-1) or res<pow(-2,31):
        return 0
     else:
          return res