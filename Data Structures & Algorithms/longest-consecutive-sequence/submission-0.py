class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_sequence = 0

        seen = {}

        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        for num in seen:
            
            sequence = 1
            n = num + 1

            while n in seen:

                n += 1
                sequence += 1

            longest_sequence = max(longest_sequence, sequence)

        return longest_sequence

            
            


        