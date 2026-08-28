class Solution:
    def trap(self, height: List[int]) -> int:
        n =len(height)
        left = 0 
        right = n-1 
        left_max = height[0]
        right_max = height[n-1]
        water_sum = 0 
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max,height[left])
                water_sum += left_max -height[left]
            else:
                right -= 1
                right_max = max(height[right],right_max)
                water_sum += right_max - height[right]
        return water_sum 
