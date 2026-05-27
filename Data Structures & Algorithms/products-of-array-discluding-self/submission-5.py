class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []

        num_zeroes = 0
        for num in nums:
            if num == 0:
                num_zeroes += 1
                continue
            product *= num
        
        # [0, 8, 0] --> [0, 0, 0]
    
        for num in nums:
            if num_zeroes == 0:
                output.append(int(product / num))
            elif num_zeroes == 1:
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            else: # num_zeroes >= 2
                output.append(0)
        
        return output
    # time complexity: O(n)
    # space complexity: O(n)



