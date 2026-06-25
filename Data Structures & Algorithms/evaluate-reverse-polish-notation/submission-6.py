import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op = '+-*/'
        stack = []

        for token in tokens:

            if token in op:

                opd_2, opd_1 = stack.pop(), stack.pop()
                operation = opd_1 + token + opd_2
                result = eval(operation)

                if token == '/' and result > 0:
                    result = math.floor(result)

                elif token == '/' and result < 0:
                    result = math.ceil(result)

                stack.append(str(result))

            else:

                stack.append(token)
            
        return int(eval(stack.pop()))