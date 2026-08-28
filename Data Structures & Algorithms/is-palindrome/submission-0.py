class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = []
        for c in s:
            if c.isalnum():
                char.append(c.lower())
        if char == char[::-1]:
            return True 
        return False 