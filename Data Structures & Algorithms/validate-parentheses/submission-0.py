class Solution:
    def isValid(self, s: str) -> bool:
       mp = {")":"(","]":"[","}":"{"} 
       stack = []
       for ch in s: 
        if ch in "{[(":
            stack.append(ch)
        else:
                if not stack:
                    return False 
                else:
                    if mp[ch] == stack[-1]:
                        stack.pop()
                    else:
                        return False 
       return not stack 
