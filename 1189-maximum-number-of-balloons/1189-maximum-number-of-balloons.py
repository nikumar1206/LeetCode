class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0,
        }
        for char in text:
            if char in char_count:
                char_count[char] += 1
        
        char_count["l"] = int(char_count["l"]/2)
        char_count["o"] = int(char_count["o"]/2)
        
        return min(char_count.values())
        