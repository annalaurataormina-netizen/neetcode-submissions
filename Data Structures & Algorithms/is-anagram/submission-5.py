class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # The key is to use dictionaries because
        # they allow O(1) lookup.
        s_chars = {}
        t_chars = {}

        for char in s:
            s_chars[char] = s_chars.get(char, 0) + 1
        
        for char in t:
            t_chars[char] = t_chars.get(char, 0) + 1

        if s_chars.items() == t_chars.items():
            return True

        return False


        