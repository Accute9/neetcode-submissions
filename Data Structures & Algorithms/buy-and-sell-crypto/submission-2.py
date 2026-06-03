class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = left + 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left += 1
                continue
            max_profit = max(max_profit, profit)
            right += 1
        return max_profit

    # Time Complexity: O(n), iterating thru array one time
    # Space Complexity: O(1), no new space created