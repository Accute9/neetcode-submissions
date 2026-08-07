class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_hours = max(piles)
        low, high = 1, (max_hours + 1)
        min_k = high
        while low <= high:
            mid = int ((low + high) / 2)
            print("MID: ", mid)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours > h: # k is too small
                low = mid + 1
            else:
                min_k = min(min_k, mid)
                high = mid - 1
        return min_k

# Time complexity: O(nlogm) where n is number of piles, m is max pile
# Space compelxity: O(1), don't need an array to actually do the binary search, can just work with numbers
         
            