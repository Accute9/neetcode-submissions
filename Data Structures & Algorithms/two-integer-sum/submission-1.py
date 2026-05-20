class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check if target - nums exists
        # {number: index}
        num_map = {}
        index = 0
        output_list = [0, 1]
        for num in nums:
            if target - num in num_map:
                output_list[0] = num_map[target - num]
                output_list[1] = index
                return output_list
            num_map[num] = index
            index += 1
        return output_list