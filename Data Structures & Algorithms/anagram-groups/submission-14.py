class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Default dictionary where the default value is an empty list.
        result = defaultdict(list)

        for s in strs:
            
            # List of 26 0's
            count = [0] * 26

            # ord('c') returns the ASCII of character 'a'
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Convert the list to a tuple to use it as key in the dictionary.
            result[tuple(count)].append(s)

        return list(result.values())