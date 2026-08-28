class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0 
        ans = 0
        n = len(s)
        for right in range(n):
            count[s[right]] = count.get(s[right],0) + 1
            max_count = max(count.values())
            while right - left - max_count + 1 > k:
                count[s[left]] -= 1
                max_count = max(count.values())
                left += 1
            ans = max(ans,right-left+1)
        return ans 
