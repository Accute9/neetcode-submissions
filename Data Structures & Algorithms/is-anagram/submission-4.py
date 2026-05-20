class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        # Use hashmap: {letter: count} for both strings b/c we know length is equal, and then compare them to check for content equality
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 0
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 0
        if s_dict == t_dict:
            return True
        return False
        # Time Complexity: O(n)
        # Space Complexity: O(n)