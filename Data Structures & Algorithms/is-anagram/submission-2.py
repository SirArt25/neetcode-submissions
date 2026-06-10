class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_counts = [0] * 26
        for char in s:
            letter_counts[ord(char) - ord('a')] += 1
        for char in t:
            if letter_counts[ord(char) - ord('a')] == 0:
                return False
            letter_counts[ord(char) - ord('a')] -= 1
        return True