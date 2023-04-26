class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # my first solution
        # for _ in range(len(nums)):
        #     if val in nums:
        #         nums.remove(val)
        # return len(nums)
        # use a while loop  ensures that we only do the in operation as long as the value is still in nums
        while val in nums:
            nums.remove(val)
        return len(nums)