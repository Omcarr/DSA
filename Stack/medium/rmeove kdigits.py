class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and k>0 and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        
        if k:
            stack=stack[:-k]

        res=''.join(stack).lstrip('0')
        if res:
            return res
        else:
            return '0'

          

        