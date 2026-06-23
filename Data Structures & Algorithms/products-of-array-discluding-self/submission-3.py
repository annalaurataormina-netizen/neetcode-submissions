class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = []
        result = []
        
        if not nums:
            return 1

        prefix.append(nums[0])
        postfix.append(nums[-1])

        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i-1])

        for i in range(0, len(nums)-1):
            postfix.append(nums[len(nums)-2-i] * postfix[i])

        postfix = postfix[::-1]

        result.append(postfix[1])

        for i in range(1, len(nums)-1):
            result.append(prefix[i-1] * postfix[i+1])

        result.append(prefix[len(nums)-2])

        return result

            

        
