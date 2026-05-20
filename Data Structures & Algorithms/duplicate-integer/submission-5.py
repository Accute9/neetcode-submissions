class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False

# Time Complexity: O(n) because you are iterating through the entire array
# Space Complexity: O(n) because the set hash_set grows linearly as the array is traversed