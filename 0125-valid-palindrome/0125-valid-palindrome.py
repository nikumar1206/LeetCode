class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char
        cleaned_string = cleaned_string.lower()
        return cleaned_string[::-1] == cleaned_string