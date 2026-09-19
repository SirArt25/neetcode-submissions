class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, right = 0, 0
        characters = set([s[0]])
        max_size = 1
        while right < len(s):
            if right < (len(s) - 1) and s[right+1] not in characters:
                right += 1
                characters.add(s[right])
                max_size = max(max_size, right - left + 1)
            elif left < len(s):
                characters.remove(s[left])
                left += 1
            else:
                break

        return max_size