class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        triplets = set() # set of tuples

        for i, n in enumerate(nums[:-2]):

            j = i + 1
            k = len(nums)-1

            while k - j >= 1:
                
                tot = nums[i] + nums[j] + nums[k]

                if tot == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                
                elif tot > 0:
                    k -= 1

                elif tot < 0:
                    j += 1
            
        return list([list(t) for t in triplets])