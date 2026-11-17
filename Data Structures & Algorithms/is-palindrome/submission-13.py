import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = 0
        backward = len(s)-1

        if len(s) == 1:
            return True

        for i in range(len(s)):
            while forward < len(s) and not s[forward].isalnum():
                forward += 1
            while backward > 0 and not s[backward].isalnum():
                backward -= 1
            if forward < len(s) and backward > 0 and s[forward].lower() != s[backward].lower():
                return False
            forward += 1
            backward -= 1

        return True