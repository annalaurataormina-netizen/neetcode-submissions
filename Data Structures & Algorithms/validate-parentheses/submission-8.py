class Solution:
    def isValid(self, s: str) -> bool:

        closing = {'(': ')', '[': ']', '{': '}'}

        order = []

        for c in s:
            
            if c in closing.keys():
                order.insert(0, closing[c])
            elif c in closing.values() and order and order[0] == c:
                order.pop(0)
            else:
                return False

        if not order:
            return True

        return False        