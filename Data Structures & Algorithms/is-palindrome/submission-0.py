import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces_string = s.replace(" ", "")
        lowercase_string = no_spaces_string.lower()
        stripped_string = ''.join(char for char in lowercase_string if char not in string.punctuation)
        reversed_s = stripped_string[::-1]


        if reversed_s == stripped_string:
            return True
        else:
            return False
