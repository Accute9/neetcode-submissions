class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {str: [str1, str2, str3]}
        # {stop: [stop, pots]} tops sort(tops) - key
        # sort str,

        ### FIRST SOLUTION - NOT OPTIMAL
        # string_map = {}
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if sorted_s in string_map:
        #         string_map[sorted_s].append(s)
        #     else:
        #         string_map[sorted_s] = [s]
        # output_list = []
        # for key in string_map:
        #     output_list.append(string_map[key])
        # return output_list




        # time complexity: O(nlog(n) + m) where n is the length of the string and m is the number of strings
        # space complexity: O(n * m) where n is the number of strings, m is the length of the longest string for worst case

        # Frequency of each char in a string
        # [0, 0, 0, 0, 0, ... 26]

        ### SECOND SOLUTION
        string_map = {}
        for s in strs:
            char_freq = [0 for i in range(26)]
            for char in s:
                char_freq[ord(char) - ord('a')] += 1
            char_freq = tuple(char_freq)
            if char_freq in string_map:
                string_map[char_freq].append(s)
            else:
                string_map[char_freq] = [s]
        output_list = []
        for freq in string_map:
            output_list.append(string_map[freq])
        return output_list

    

