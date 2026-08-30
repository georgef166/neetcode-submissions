import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(filter(str.isalnum, s))
        lowercase_text = cleaned_text.lower()
        reversed_text = lowercase_text[::-1]
        
        if lowercase_text == reversed_text:
            return True
        return False