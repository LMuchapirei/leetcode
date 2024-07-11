class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0

        for log in logs:
            if log == "../":
                res = max(res,res-1)
            elif log == "./":
                continue
            else:
                res += 1
        return res


"""
My rather complicated solution first
import re
# from collections import deque
# Define the regex pattern
pattern = re.compile(r'[a-zA-Z0-9]+/')
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # stack = deque()
        count = 0
        for op in logs:
            if op != "../" and len(op.split("/")) == 2:
                count += 1
                # stack.append(op)
            elif op == "../":
                if count != 0:
                    count -= 1
                # if len(stack):
                #     stack.pop()
            else:
                continue

        return count #len(stack)
        # ["d1/","d2/","../","d21/","./"]
        # goDeep(example d1/) --> add element to stack
        # remain(./) --> stay at the current level
        # goBack(../) --> pop the current element on top of the stack
        # after all operations count number of elements inside of the stack
        # [d1]
        # [d2,d1]
        # [d1]
        # [d21,d1]
        # len(2)
"""