class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        chars = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        if s[0] not in chars:
            return False

        for x in s:
            if x in chars:
                stack.append(x)

            else:
                if stack: 
                    temp = stack.pop()
                    if x != chars[temp]:
                        return False
                else: 
                    return False
                

        return not stack
                
            