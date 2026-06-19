class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = defaultdict(int)

        for n in nums:
            seen[n] += 1

    
        print(seen.items())

        seen = {k: v for k, v in sorted(seen.items(), key = lambda x: x[1], reverse = True)}

        print(seen)

        return list(seen.keys())[:min(len(seen), k)]