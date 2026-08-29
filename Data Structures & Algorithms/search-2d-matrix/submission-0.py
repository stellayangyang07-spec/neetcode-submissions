class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target > matrix[i][n-1]:
                continue 
            left = 0 
            right = n-1
            while left <= right:
                mid = (left+right) // 2
                if target < matrix[i][mid]:
                    right = mid-1 
                elif target > matrix[i][mid]:
                    left = mid+1
                else:
                    return True 
        return False 
