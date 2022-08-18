class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_len = 0
        while j < len(s):
            substr = s[i:j+1]
            if len(substr) == len(set(substr)):
                max_len = max(len(substr), max_len)
            else:
                i += 1
            j += 1  
        return max_len