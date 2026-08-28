class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0 
        right = 0 
        max_length = 0
        n = len(s)
        while right < n:
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(right-left+1,max_length)
            right += 1
        return max_length 

            

