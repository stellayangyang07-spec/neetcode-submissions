class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_fix = stack.pop()
                ans[pre_fix] = i-pre_fix
            stack.append(i)
        return ans 