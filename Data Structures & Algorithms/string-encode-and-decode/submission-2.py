class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += string
            res += f"ln:"
        return res
    def decode(self, s: str) -> List[str]:
        strs = []
        string = ""
        count = 0
        for i in range(len(s)):
            if count > 0 and count < 3:
                count += 1
                next
            else:
                count = 0
                string += s[i]
            if s[i] == "l" and s[i+1] == "n" and s[i+2] == ":":
                strs.append(string[:-1])
                string = ""
                count += 1
        return strs
