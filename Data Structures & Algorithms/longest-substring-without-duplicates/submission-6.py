class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l, r, char_set, longest_sequence = 0, 0, set(), 0

        while l < len(s) and r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            r += 1
            longest_sequence = max(longest_sequence, len(char_set))

        return longest_sequence