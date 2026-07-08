import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i <= j:
            
            if not isalnum(s[i]):
                i += 1
                continue
            
            if not isalnum(s[j]):
                j -= 1
                continue

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True