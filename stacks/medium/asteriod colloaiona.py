class Solution:
    def asteroidCollision(self, a: list[int]) -> list[int]:
        stack=[]
        for i in a:
            while stack and i < 0 and stack[-1]> 0:
                diff= i+stack[-1]
                if diff>0:
                    i=0
                elif diff<0:
                    stack.pop()
                else:
                    i=0
                    stack.pop()
            if i:
                stack.append(i)
        return stack
        