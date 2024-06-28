class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            # call the routine and return the first entry thats a palindrome
            if self.isPalindrome(s):
                return s
        return ""

    def isPalindrome(self,s):
        # s[::-1] reverse a string in python
        # we check after reversing s in this case we get a reversed copy 
        # we check if its equal with original unchanged s
        # return the boolean check result
        return s[::-1] == s
    
    def isPalindromePointer(self,s):
        ## Seems the first example is more efficient than this one according to leetcode runtime
        l,r = 0,len(s)-1
        while l < r:
            if s[l] == s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

