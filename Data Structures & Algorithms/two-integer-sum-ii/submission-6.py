class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while (l < r):
            if (numbers[l] + numbers[r] > target):
                r -= 1
            elif (numbers[l] + numbers[r] < target):
                l += 1
            else:
                break
        output = []
        output.append(l + 1)
        output.append(r + 1)
        return output

    # Time complexity: O(n) - both l and r can move at most n times
    # Space complexity: O(1), output grows by 2 elements every time algorithm is called - constant