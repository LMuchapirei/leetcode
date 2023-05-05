class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # using the sliding pointer technique to solve this one
        # window size will be k
        # we shift this window when some conditions are met
        # we then keep track of the count of vowels we have seen and then update it when we encounter a more larger value of count
        vowelsSet = {'a','e','i','o','u'}
        l,cnt,res=0,0,0
        for r in range(len(s)):
            cnt +=1 if s[r] in vowelsSet else 0
            if r-l +1  > k:
                cnt -= 1 if s[l] in vowelsSet else 0
                l += 1
            res = max(res,cnt)
        return res