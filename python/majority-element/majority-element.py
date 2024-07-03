from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] = cnt.get(i,1) + 1
        return max(cnt, key=cnt.get)