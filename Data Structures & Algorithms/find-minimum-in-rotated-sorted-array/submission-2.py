class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        min_num = 1001
        # check which side of the array is sorted
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]: # number is right of mid
                low = mid + 1
                if nums[mid] < min_num:
                    min_num = nums[mid]
            else:
                high = mid - 1
                if nums[mid] < min_num:
                    min_num = nums[mid]
        return min_num
        # Time Complexity: O(log n)
        # Space Complexity: O(1)