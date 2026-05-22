class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_map = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in valid_map: # use peek to check if valid
                if stack and (stack[-1] == valid_map[ch]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if (not stack):
            return True
        return False