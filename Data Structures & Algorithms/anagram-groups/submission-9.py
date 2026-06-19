class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        chars_by_string = {}
        strings = {}

        for string in strs:

            if string in chars_by_string:
                strings[string] += 1
                continue

            strings[string] = 1
            chars = {}
            
            for char in string:

                chars[char] = chars.get(char, 0) + 1

            chars_by_string[string] = chars

        my_list = []

        for k, v in chars_by_string.items():
            
            added = False

            for sublist in range(len(my_list)):

                equal = True

                if chars_by_string[k] != chars_by_string[my_list[sublist][0]]:
                    equal = False

                if equal:
                    for i in range(strings[k]):
                        my_list[sublist].append(k)
                    added = True
                    break

            if not added:
                new_list = []
                for i in range(strings[k]):
                    new_list.append(k)
                my_list.append(new_list)
        
        return my_list




                

            


        


