class Solution:
    def maxUncrossedLines(self,nums1,nums2):
        
        def dfs(i,j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if nums1[i]==nums2[j]:
               return  1 + dfs(i+1,j+1)
            else:
               return  max(dfs(i+1,j),
                dfs(i,j+1))
        dp = {}

        return dfs(0,0)
        # O(n * m) space complexity
        # 0(n*n) time complexity
        # We used memoization 


    def maxUncrossedLinesTabulation(self,nums1,nums2):
        prev = [0] * (len(nums2)+1) 

        for i in range(len(nums1)):
            dp = [0] * (len(nums2)+1)
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    dp[j+1]=1 + prev[j]
                else:
                    dp[j+1]= max(
                        dp[j],
                        prev[j+1]
                    )
            prev = dp
        return prev[len(nums2)]
