class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_cleaned = s.upper().replace(' ', '').replace('?', '').replace(',', '').replace("'", '').replace('.', '').replace(':', '')

        print(s_cleaned)

        l = len(s_cleaned)

        for i in range(l):
            if s_cleaned[i] != s_cleaned[l - i - 1]:
                return False

        return True
