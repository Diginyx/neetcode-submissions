class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        t_hash = dict()

        for letter in s:
            str_letter = str(letter)
            if not str_letter in s_hash:
                s_hash[str_letter] = 0
            s_hash[str_letter] += 1
        for letter in t:
            str_letter = str(letter)
            if not str_letter in t_hash:
                t_hash[str_letter] = 0
            t_hash[str_letter] += 1

        if s_hash == t_hash:
            return True
        else: 
            return False