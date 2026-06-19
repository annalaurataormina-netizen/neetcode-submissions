class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # The key is to use a dictionary with int as key and index as value
        # because it allows O(1) lookup.
        occurrences = {}

        for i, n in enumerate(nums):
            
            # Look for the difference to make the target.
            diff = target - n

            if diff in occurrences:
                return [occurrences[diff], i]

            occurrences[n] = i

        