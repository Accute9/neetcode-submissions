class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0): return 0
        left = 0
        right = 0
        max_length = 1
        seen = set(s[left])
        while right < len(s):
            right += 1
            if right >= len(s):
                break
            if s[right] in seen and right != left:
                while s[right] in seen and left < right:
                    seen.discard(s[left])
                    left += 1
            seen.add(s[right])
            length = right - left + 1
            max_length = max(length, max_length)
        return max_length

        # Time complexity: O(n), as both pointers continue to move forward until n - 1
        # Space complexity: O(m) where m is the number of unique chars in the string
            

