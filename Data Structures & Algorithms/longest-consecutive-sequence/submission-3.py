class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set()
        seen = set()
        max_length = 1
        length = 1
        for num in nums:
            num_set.add(num)
        for num in num_set:
            if not num - 1 in num_set: # beginning of theoretical sequence
                length = 1
                while num + 1 in num_set:
                    length += 1
                    num += 1
                max_length = max(max_length, length)
        return max_length
                

