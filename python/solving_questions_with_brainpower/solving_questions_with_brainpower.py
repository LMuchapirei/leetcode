class Solution:
    # Zero-One knapsack problem
    def mostPoints(self,questions):
        # Time : O(N)
        # Space : O(N)
        dp = {}
        def dfs(i):
            if i >= len(questions):
                return 0
            if i in dp:
                return dp[i]
            dp[i]=max(dfs(i+1), # skip question
            questions[i][0] + dfs(i+1+questions[i][1]))

            return dp[i]
        return dfs(0)
    
    def mostPointsTabular(self,questions):
        dp = { }
        for i in range(len(questions)-1,-1,-1):
            dp[i] = max(questions[i][0] + dp.get(i+1+questions[i][1],0), #include current question
                        dp.get(i+1,0))  # skip
        return dp[0]