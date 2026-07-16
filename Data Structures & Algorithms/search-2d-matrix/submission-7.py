class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = -1
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            
            middle = (top + bottom) // 2

            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                row = middle
                break

            if top == bottom:
                return False

            if target > matrix[middle][-1]:
                top = middle + 1

            elif target < matrix[middle][0]:
                bottom = middle - 1

        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            
            middle = (left + right) // 2

            if matrix[row][middle] == target:
                return True

            if left == right:
                return False

            if target > matrix[row][middle]:
                left = middle + 1

            else:
                right = middle - 1
    
        return False