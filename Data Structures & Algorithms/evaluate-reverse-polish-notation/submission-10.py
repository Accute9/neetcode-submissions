class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == "+":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(num_1 + num_2)
            elif item == "-":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(num_2 - num_1)
            elif item == "*":
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(num_1 * num_2)
            elif item == "/":
                if (stack[-1] == 0):
                    continue
                num_1 = stack.pop()
                num_2 = stack.pop()
                stack.append(int(num_2 / num_1))
            else:
                stack.append(int(item))
        return stack.pop()
    
    # Time complexity: O(n), iterates thru array one time
    # Space complexity: O(n), in worst case stack grows linearly with time