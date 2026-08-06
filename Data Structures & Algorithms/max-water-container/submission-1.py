class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        max_amount = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            cur_amount = min(heights[l], heights[r]) * (r - l)
            max_amount = max(cur_amount, max_amount)
            if heights[l] < heights[r]:
                l += 1
                continue
            else:
                r -=1
        return max_amount

# O(n) time, going thru array once
# O(1) space, not storing anything besides ints