class Solution:

    def maxScore(self,nums):

        cache = collections.defaultdict(int)
        # O(n^2* 2^n * logM)
        # loops nested n ^2
        # the recursion 2^n
        # the gcd calculation logM
        def dfs(mask,op):
            if mask in cache:
                return cache[mask]
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue
                    newMask  = mask | (1 << i) | (1 << j)
                    score = op * math.gcd(nums[i],nums[j])
                    cache[mask] = max(
                        cache[mask],
                        score + dfs(newMask,op +1))
            return cache[mask]
        return dfs(0,1)