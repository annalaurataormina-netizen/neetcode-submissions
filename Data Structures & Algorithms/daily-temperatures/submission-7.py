class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        i = len(temperatures)-2
        result = [0]
        stack = [(temperatures[-1], len(temperatures)-1)]

        while i >= 0:
            
            print(temperatures[i])

            if temperatures[i] > temperatures[i + 1]:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if stack:
                    result.insert(0, stack[-1][1] - i)
                else:
                    result.insert(0, 0)
                stack.append((temperatures[i], i))

            elif temperatures[i] == temperatures[i + 1]:
                result.insert(0, result[0] + 1 if result[0] > 0 else 0)
                stack.pop()
                stack.append((temperatures[i], i))

            elif temperatures[i] < temperatures[i+1]:
                result.insert(0, 1)
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                stack.append((temperatures[i], i))

            i -= 1

            print(result)
            print(stack)

        return result



