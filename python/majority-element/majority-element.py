from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] = cnt.get(i,1) + 1
        return max(cnt, key=cnt.get)
    

    # 'Boyer-Moore Voting' algorithm does it in O(1)
    def majorityElementO_1(self,nums:List[int]) -> int:
        res,count = 0,0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
    def majorityElementRecur(self, nums: List[int]) -> int:
        def majority_element_rec(start, end):
            # Base case: the single element in this subarray
            if start == end:
                return nums[start]

            # Recur for left and right halves
            mid = (start + end) // 2
            left_majority = majority_element_rec(start, mid)
            right_majority = majority_element_rec(mid + 1, end)

            # If the two halves agree on the majority element, return it
            if left_majority == right_majority:
                return left_majority

            # Otherwise, count each element and return the "winner"
            left_count = sum(1 for i in range(start, end + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(start, end + 1) if nums[i] == right_majority)

            return left_majority if left_count > right_count else right_majority

        return majority_element_rec(0, len(nums) - 1)

