class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        i = len(temperatures)-2
        result = [0]
        stack = [(temperatures[-1], len(temperatures)-1)]

        while i >= 0:

            print(temperatures[i])
            
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if temperatures[i] > temperatures[i + 1]:
                result.append(stack[-1][1] - i if stack else 0)

            elif temperatures[i] == temperatures[i + 1]:
                result.append(result[-1] + 1 if result[-1] > 0 else 0)

            elif temperatures[i] < temperatures[i+1]:
                result.append(1)

            stack.append((temperatures[i], i))

            print(result)
            print(stack)

            i -= 1

        return result[::-1]