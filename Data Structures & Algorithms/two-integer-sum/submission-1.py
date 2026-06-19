class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        occurrences = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in occurrences:
                return [occurrences[diff], i]

            occurrences[n] = i

        