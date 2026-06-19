class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # The key is to use a dictionary because
        # it allows O(1) lookup.
        nums_occurrences = {}

        for num in nums:
            
            if num in nums_occurrences:
                return True

            else:
                nums_occurrences[num] = 1

        return False