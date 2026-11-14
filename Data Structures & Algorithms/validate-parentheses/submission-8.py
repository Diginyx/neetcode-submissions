class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partner = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in partner:
                if stack and stack[-1] == partner[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
