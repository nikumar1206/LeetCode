from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      seen = {}
      for word in strs:
        rearranged_word = "".join(sorted(word))
        if rearranged_word in seen:
          seen[rearranged_word].append(word)
        else:
          seen[rearranged_word] = [word]
      return list(seen.values())