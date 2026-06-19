class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_occurrences = {}

        for num in nums:

            if num in nums_occurrences:
                return True

            else:
                nums_occurrences[num] = 1

        return False



        