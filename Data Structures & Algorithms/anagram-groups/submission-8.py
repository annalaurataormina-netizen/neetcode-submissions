class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        chars_by_string = {}

        for string in strs:

            if string in chars_by_string:
                chars_by_string[string]['num'] += 1
                continue

            chars = {'num': 1}
            
            for char in string:

                chars[char] = chars.get(char, 0) + 1

            chars_by_string[string] = chars

        my_list = []

        for k, v in chars_by_string.items():
            
            added = False

            for sublist in range(len(my_list)):

                equal = True
                
                for char in k:

                    if chars_by_string[k][char] != chars_by_string[my_list[sublist][0]].get(char, 0):
                        equal = False
                        break

                for char in my_list[sublist][0]:

                    if chars_by_string[k].get(char, 0) != chars_by_string[my_list[sublist][0]][char]:
                        equal = False
                        break

                if equal:
                    for i in range(chars_by_string[k]['num']):
                        my_list[sublist].append(k)
                    added = True
                    break

            if not added:
                new_list = []
                for i in range(chars_by_string[k]['num']):
                    new_list.append(k)
                my_list.append(new_list)
        
        return my_list




                

            


        


