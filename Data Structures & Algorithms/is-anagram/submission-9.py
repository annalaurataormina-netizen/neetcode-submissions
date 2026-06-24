class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_chars = defaultdict(int)
        t_chars = defaultdict(int)

        for char in s:
            s_chars[char] = s_chars[char] + 1
        
        for char in t:
            t_chars[char] = t_chars[char] + 1

        return s_chars == t_chars