class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        arr.sort()
        prev = 0
        for n in arr:
            prev = min(prev+1,n)
        return prev


