class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        triplets = set() # set of tuples

        print(nums)

        for i, n in enumerate(nums[:-2]):

            j = i + 1
            k = len(nums)-1

            while k - j >= 1:

                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1


                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
            
        return list([list(t) for t in triplets])