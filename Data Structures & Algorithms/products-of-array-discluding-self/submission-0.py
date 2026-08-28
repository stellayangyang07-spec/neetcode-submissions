class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = 1
        ans = [1] * n
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]
        right_product = 1 
        for j in range(n-1,-1,-1):
            ans[j] *= right_product 
            right_product *= nums[j]
        return ans 
