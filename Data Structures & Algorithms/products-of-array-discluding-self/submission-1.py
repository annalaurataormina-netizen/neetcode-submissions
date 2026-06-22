class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        total = 1
        zeroes = 0

        for num in nums:
            if num == 0:
                zeroes += 1
                continue
            total *= num

        if zeroes > 1:
            total = 0

        for num in nums:
            if num == 0:
                result.append(total)
            elif zeroes >= 1:
                result.append(0)
            else:
                result.append(total//num)

        return result

        

        