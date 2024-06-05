class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack=[len(t)-1]
        res=[0]*(len(t))
        for i in range(len(t)-2,-1,-1):
            while stack and t[i]>=t[stack[-1]]:
                stack.pop()

            if stack:
                res[i]=stack[-1]-i

            stack.append(i)
        return res
