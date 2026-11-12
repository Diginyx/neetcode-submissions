class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freqChars = [0] * 26
            for char in string:
                number = (ord(char) - 96) - 1
                freqChars[number] += 1
            key = tuple(freqChars)
            if key not in anagrams:
                anagrams[key] = [string]
            else:
                anagrams[key].append(string)
        
        real_anagrams = []
        for key in anagrams:
            real_anagrams.append(anagrams[key])
        
        return real_anagrams
        