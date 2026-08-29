import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        while left <= right:
            mid = (left+right) // 2
            time_sum = 0 
            for pile in piles:
                time_sum += math.ceil(pile / mid)
            if time_sum > h:
                left = mid+1 
            else:
                right = mid-1
        return left 
