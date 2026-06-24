class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0: return 0
        left = 0
        right = 0
        max_length = 1
        cur_length = 1
        temp_k = k
        char_freq = {s[left]: 1}
        while right < len(s):
            right += 1
            if right >= len(s):
                break
            if s[right] in char_freq:
                char_freq[(s[right])] += 1
            else:
                char_freq[(s[right])] = 1
            max_freq = max(char_freq.values())
            num_replacements = (right - left + 1) - max_freq
            if num_replacements <= k:
                cur_length += 1
                max_length = max(max_length, cur_length)
            else:
                while num_replacements > k:
                    char_freq[(s[left])] -= 1
                    left += 1
                    cur_length = right - left + 1
                    num_replacements = cur_length - max(char_freq.values())
        return max_length
        
        # Time complexity: O(n)
        # Space complexity: O(m), hashmap grows linearly as string is traversed



