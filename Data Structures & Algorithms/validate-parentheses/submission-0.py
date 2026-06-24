class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        character_map = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        for char in s:
            if char in character_map:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last = stack[-1]
                stack.pop()
                if character_map[last] != char:
                    return False




        return len(stack) == 0