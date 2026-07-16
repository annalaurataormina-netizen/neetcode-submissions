class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums)-1

        while end >= start:
            
            middle = (end + start) // 2

            if nums[middle] == target:
                return middle

            if end == start:
                return -1

            if target > nums[middle]:
                start = middle + 1

            else:
                end = middle - 1
    
        return -1