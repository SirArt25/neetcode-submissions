class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_words = {}
        for word in strs:
            modified = "".join(sorted(word))
            if modified not in dict_words:
                dict_words[modified] = []

            dict_words[modified].append(word)
            
        result = []
        for key, values in dict_words.items():
            result.append(values)
        return result