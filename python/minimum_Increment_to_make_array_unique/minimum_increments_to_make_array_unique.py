from collections import defaultdict
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # minValue = min(nums)
        # maxValue = max(nums)
        # print(f"This is the min val {minValue} and max Value {maxValue}")
        # fillArray = [i for i in range(minValue,maxValue + 2)]
        # duplicate = defaultdict(list)
        # for i,val in enumerate(nums):
        #     if val in duplicate:
        #         duplicate[val].append(i)
        #     else:
        #         duplicate[val] = [i]
        # print(fillArray)
        # print(nums)
        # fillValues = list(set(fillArray).difference(set(nums)))
        # print(fillValues)
        # count = 0
        # for dupKey in duplicate.keys():
        #     numberOfApp = len(duplicate[dupKey])-1
        #     for i in range(numberOfApp):
        #         minVal = min(fillValues)
        #         fillValues.remove(minVal)
        #         if minVal < dupKey:
        #             continue
        #         count += (minVal-dupKey)
        # return count

        # Simpler solution
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                res += 1 + (nums[i-1] - nums[i])
                nums[i] = nums[i-1] + 1
        return res


sltn  = Solution()
c = sltn.minIncrementForUnique(nums=[0,2,2])
print(c)