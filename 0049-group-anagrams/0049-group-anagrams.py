from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}
        for string in strs:
            converted = "".join(sorted(string))
            if converted not in string_dict:
                string_dict[converted] = [string]
            else:
                string_dict[converted].append(string)
        return list(string_dict.values())
                    