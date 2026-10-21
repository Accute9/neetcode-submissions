class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        left, right = 0, 0
        max_length = 0
        max_freq = 0
        char_freq = collections.defaultdict(int)
        char_freq[s[left]] += 1
        while right < len(s) - 1:
            right += 1
            char_freq[s[right]] += 1
            max_freq = max(max_freq, char_freq[s[right]])
            len_window = right - left + 1
            if len_window - max_freq <= k:
                max_length = max(max_length, len_window)
                continue
            else:
                while len_window - max_freq > k and left < right:
                    if char_freq[s[left]] > 1:
                        char_freq[s[left]] -= 1
                    else:
                        del char_freq[s[left]]
                    left += 1
                    len_window = right - left + 1
                    max_length = max(max_length, len_window)
                    max_freq = max(char_freq.values())
        return max_length
        

        """
        For a given window, the number of replacable characters = the total number of chars - max frequency in char_freq
        If this difference is less than k, we have a valid window

        XXYYZZ, k = 3

        XYYXYYYYX K = 1

        """
            
