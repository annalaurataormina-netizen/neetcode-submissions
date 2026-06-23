class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        starts = []

        print(nums)

        for n in nums:
            if (n - 1) not in nums:
                starts.append(n)

        starts = set(starts)

        longest_sequence = 0

        for start in starts:
            n = start + 1
            sequence = 1

            while n in nums:
                sequence += 1
                n += 1

            longest_sequence = max(longest_sequence, sequence)

        return longest_sequence

        