import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        return False
        