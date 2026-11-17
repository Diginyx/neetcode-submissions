import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = 0
        backward = len(s)-1

        if len(s) == 1:
            return True

        while forward < backward:
            while forward < backward and not s[forward].isalnum():
                forward += 1
            while backward > forward and not s[backward].isalnum():
                backward -= 1
            if s[forward].lower() != s[backward].lower():
                return False
            forward += 1
            backward -= 1

        return True