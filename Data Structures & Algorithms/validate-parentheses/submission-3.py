class Solution:
    def isValid(self, s: str) -> bool:

        parentheses = False
        square = False
        curly = False
        order = []

        for c in s:
            if c == '(' and parentheses == False:
                parentheses = True
                order.insert(0, ')')
            elif c == '[' and square == False:
                square = True
                order.insert(0, ']')
            elif c == '{' and curly == False:
                curly = True
                order.insert(0, '}')
            elif c == ')' and parentheses == True and order[0] == c:
                parentheses = False
                order.pop(0)
            elif c == ']' and square == True and order[0] == c:
                square = False
                order.pop(0)
            elif c == '}' and curly == True and order[0] == c:
                curly = False
                order.pop(0)
            else:
                return False

        if not parentheses and not square and not curly:
            return True

        return False        


        