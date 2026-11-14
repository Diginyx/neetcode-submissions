class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        partner = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char not in partner:
                stack.append(char)
            else:
                if stack and stack[-1] == partner[char]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
