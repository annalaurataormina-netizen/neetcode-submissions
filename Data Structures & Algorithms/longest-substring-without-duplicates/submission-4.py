class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_sequence, i = 0, 0

        while i < len(s):\

            sequence = {}
            eos = False

            while i < len(s) and not eos:

                if s[i] not in sequence:
                    sequence[s[i]] = i
                    i += 1

                else:
                    eos = True
                    i = sequence[s[i]] + 1
                    
            longest_sequence = max(longest_sequence, len(sequence.keys()))

        return longest_sequence