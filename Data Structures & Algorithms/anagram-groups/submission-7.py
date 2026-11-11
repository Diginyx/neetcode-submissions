class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
        
        anagrams_list = []
        for anagram in anagrams:
            anagrams_list.append(anagrams[anagram])  

        return anagrams_list

       